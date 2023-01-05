from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from uuid import NAMESPACE_DNS, uuid4, uuid5
import time
from tqdm import tqdm
from json import dumps
import pickle
from datetime import datetime
from config import OUT_PATH
from lib.common.driver import get_driver
from lib.crawler.sinsang.asset import PROD_LIST_URLS, ProdListObj
from lib.crawler.sinsang.model import SinsangGarment
from lib.util.firestore import exist_db_vendor_prod_ids
from lib.logger import IoLogger
from lib.common.model import TBD


class SinsangCrawler(IoLogger):
    entry_url: str
    sinsang_id: str
    sinsang_pw: str
    driver: webdriver.Chrome
    exist_ids: set[str]
    new_ids: set[str]
    lookup_ids: set[str]
    name = "sinsang-crawler"

    def dispose(self):
        self.driver.close()
        self.driver.quit()

    def sleep(self, n: int):
        self.driver.implicitly_wait(n * 5)
        time.sleep(n)

    def __init__(self) -> None:
        super().__init__(self.name)
        self.driver = get_driver()
        self.driver.implicitly_wait(3)
        self.entry_url = "https://sinsangmarket.kr"
        self.sinsang_id = "dazzyvely"
        self.sinsang_pw = "*wldnjs0316*"
        self.exist_ids = exist_db_vendor_prod_ids()
        self.exist_cnt = 0
        self.new_ids = set()
        self.lookup_ids = set()
        self.page = 1

    def login(self):
        self.driver.get(self.entry_url)
        self.sleep(2)
        # >>> select page language >>>
        header = self.driver.find_element(
            by=By.CLASS_NAME, value="header-container")
        area_selector = header.find_element(
            by=By.CSS_SELECTOR, value="div.select-area")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(area_selector))
        area_selector.click()
        for i in self.driver.find_elements(by=By.CSS_SELECTOR, value="li.option-area__item"):
            if ("한국어" in i.text):
                i.click()
                break
        # >>> login process >>>
        self.sleep(2)
        header = self.driver.find_element(
            by=By.CLASS_NAME, value="header-container")
        ps = header.find_elements(by=By.TAG_NAME, value="p")
        for p in ps:
            if (p.text == "로그인"):
                p.click()  # 로그인 다이얼로그
                self.sleep(2)
                self.driver.find_element(
                    by=By.CSS_SELECTOR, value="input[placeholder='아이디']").send_keys(self.sinsang_id)
                self.driver.implicitly_wait(3)
                # driver.find_element(by=By.CSS_SELECTOR, value="input[type='password']]").send_keys(sinsang_pw)
                self.driver.find_element(
                    by=By.CSS_SELECTOR, value='input[placeholder="비밀번호"]').send_keys(self.sinsang_pw)
                btns = self.driver.find_element(by=By.CLASS_NAME, value="login_option").find_elements(
                    by=By.TAG_NAME, value="button")
                for btn in btns:
                    if (btn.text == "로그인"):
                        WebDriverWait(self.driver, 15).until(
                            EC.element_to_be_clickable(btn))
                        btn.click()  # 로그인!
                        # btn.send_keys(Keys.ENTER)
                        # self.driver.execute_script(
                        #     "document.querySelectorAll('.login_option button')[1].click();")
                        # self.driver.execute_script("arguments[0].click();", btn)
                        return
        raise Exception("로그인 실패(fail to login)")

    def lets_crawl(self):
        try:
            self.login()
        except Exception as e:
            self.log.error(
                f"occurred while login, url: {self.entry_url} error: {e}")
            self.l(self.driver.get(self.entry_url))
            self.sleep(2)
            el = self.driver.find_element(by=By.TAG_NAME, value="body")
            self.log.warning(f"url element text: {el.text}")
            raise e
        self.sleep(3)
        t_bar = tqdm(PROD_LIST_URLS)
        for i, obj in enumerate(t_bar):
            desc = f"process sinsang crawler {obj.part}, {obj.ctgr}, {obj.gender}, max_page: {obj.max_page}, idx: {i} url: {obj.url}"
            t_bar.set_description(desc=desc)
            self.log.info(desc)
            try:
                garments = self.crawl_prod_list(obj)
                if len(garments) > 0:
                    with open(file=f"{OUT_PATH}/sinsang_{obj.gender}_{obj.part}_{obj.ctgr}_{datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}.pkl", mode='wb') as f:
                        pickle.dump({
                            "garments": garments,
                            "lookup_ids": self.lookup_ids,
                            "new_ids": self.new_ids
                        }, f)
                self.driver.refresh()
            except Exception as e:
                self.log.error(f"while {desc} error: {e}")
                continue
            self.log.info(f"num of exist item: {self.exist_cnt}")
            self.log.info(f"num of new item: {len(list(self.new_ids))}")

        # FIXME :  Object of type datetime is not JSON serializable
        # with open("out/sinsang.json", 'w', encoding='UTF-8-sig') as outfile:
        #     gs = list(map(lambda x: x.__dict__, garments))
        #     outfile.write(
        #         dumps({"garments": gs, "lookup_ids": self.lookup_ids, "new_ids": self.new_ids}, ensure_ascii=False))

    def crawl_prod_list(self, obj: ProdListObj) -> list[SinsangGarment]:
        garments: list[SinsangGarment] = []
        self.driver.get(obj.url)
        containers = self.driver.find_elements(
            by=By.CLASS_NAME, value="ssm-goods-list")
        self.page = 1
        curr_time = datetime.now()
        while True:
            self.log.info(f"page: {self.page} start")
            for item_list_container in containers:
                item_list = item_list_container.find_elements(
                    by=By.CSS_SELECTOR, value="[data-group='goods-list']")
                for thumbnail in item_list:
                    prod_pkg_id = thumbnail.get_attribute("data-gid")
                    self.lookup_ids.add(prod_pkg_id)
                    if prod_pkg_id in self.exist_ids:
                        self.exist_cnt += 1
                        continue

                    thumbnail.click()  # open detail product
                    vendorProdName = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".goods-detail-right p.title"))).text.strip()
                    # vendorProdName = self.driver.find_element(
                    #     by=By.CSS_SELECTOR, value=".goods-detail-right p.title").text.strip()
                    price_str = self.driver.find_element(
                        by=By.CSS_SELECTOR, value="div.price-box span").text.strip()

                    storeName = self.driver.find_element(
                        by=By.CSS_SELECTOR, value="div.store span.store__name").text.strip()

                    img_urls = []
                    for img_el in self.driver.find_elements(by=By.CSS_SELECTOR, value="div.swiper-slide img"):
                        img_urls.append(
                            img_el.get_attribute("src").strip())
                    titleImgs = [img_urls[0]]
                    bodyImgs = img_urls[1:]

                    rows = self.driver.find_elements(
                        by=By.CSS_SELECTOR, value="div.information + div > div")
                    for row in rows:
                        for div in row.find_elements(by=By.TAG_NAME, value="div"):
                            match div.text.strip():
                                case "색상":
                                    txt = row.find_element(
                                        by=By.CLASS_NAME, value="information-row__content").text
                                    colors = [color.strip()
                                              for color in txt.split(",")]
                                case "사이즈":
                                    txt = row.find_element(
                                        by=By.CLASS_NAME, value="information-row__content").text
                                    sizes = [size.strip()
                                             for size in txt.split(",")]
                                case "혼용률":
                                    fabric = row.find_element(
                                        by=By.CLASS_NAME, value="information-row__content").text.strip()
                    info = self.driver.find_element(
                        by=By.CSS_SELECTOR, value="div.information + div.row__content").text.strip()
                    entry_url = self.driver.current_url
                    tbd = TBD(storeName=storeName, linkUrl=entry_url,
                              fromWhere="SINSANG", displayFrom=True)
                    for size in sizes:
                        for color in colors:
                            garment = SinsangGarment(
                                createdAt=curr_time,
                                updatedAt=curr_time,
                                vendorProdPkgId=prod_pkg_id,
                                vendorProdId=str(
                                    uuid5(NAMESPACE_DNS, prod_pkg_id+vendorProdName+size+color)),
                                vendorProdName=vendorProdName,
                                price_str=price_str,
                                vendorPrice=-1,
                                titleImgs=titleImgs,
                                bodyImgs=bodyImgs,
                                size=size,
                                color=color,
                                fabric=fabric,
                                info=info,
                                description="description",
                                prodType="GARMENT",
                                TBD=tbd,
                                gender=obj.gender,
                                part=obj.part,
                                ctgr=obj.ctgr,
                                allowPending=False,
                                stockCnt=0)
                            garment.setPrice()
                            assert garment.is_valid == True
                            self.exist_ids.add(prod_pkg_id)
                            self.new_ids.add(prod_pkg_id)
                            garments.append(garment)

                    self.driver.find_element(
                        by=By.CSS_SELECTOR, value="img.close-button[alt='close-icon']").click()
            moreScroll = self.scrolling()
            if moreScroll == False or self.page > obj.max_page:
                self.page = 1
                break
            else:
                self.page += 1
                self.sleep(1)

        return garments

    def scrolling(self) -> bool:
        screen_height = self.driver.execute_script(
            "return window.screen.height;")
        factor = self.page * 2
        self.driver.execute_script(
            "window.scrollTo(0, {screen_height}*{factor});".format(screen_height=screen_height, factor=factor))
        # return True
        scroll_height = self.driver.execute_script(
            "return document.body.scrollHeight;")
        if ((screen_height) * self.page >= scroll_height):
            # 스롤 가능 높이보다 화면 높이가 높다면
            return False
        else:
            return True
