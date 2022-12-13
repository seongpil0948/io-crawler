from selenium import webdriver
from selenium.webdriver.common.by import By
from uuid import NAMESPACE_DNS, uuid4, uuid5
import time
from tqdm import tqdm
import pickle
from datetime import datetime
from config import OUT_PATH
from lib.common.driver import get_driver
from lib.crawler.sinsang.asset import PROD_LIST_URLS, ProdListObj
from lib.crawler.sinsang.model import SinsangGarment
from lib.util.firestore import exist_db_vendor_prod_ids

from lib.common.model import TBD


class SinsangCrawler():
    entry_url: str
    sinsang_id: str
    sinsang_pw: str
    driver: webdriver.Chrome
    exist_ids: set[str]
    new_ids: set[str]
    lookup_ids: set[str]

    def __init__(self) -> None:
        self.driver = get_driver()
        self.driver.implicitly_wait(3)
        self.entry_url = "https://sinsangmarket.kr"
        self.sinsang_id = "bereshith"
        self.sinsang_pw = "*wldnjs0316*"
        self.exist_ids = exist_db_vendor_prod_ids()
        self.exist_cnt = 0
        self.new_ids = set()
        self.lookup_ids = set()
        self.page = 1

    def login(self):
        self.driver.get(self.entry_url)
        time.sleep(2)
        # >>> select page language >>>
        header = self.driver.find_element(
            by=By.CLASS_NAME, value="header-container")
        header.find_element(by=By.CSS_SELECTOR,
                            value="div.select-area").click()
        for i in self.driver.find_elements(by=By.CSS_SELECTOR, value="li.option-area__item"):
            if ("한국어" in i.text):
                i.click()
                break
        # >>> login process >>>
        self.driver.implicitly_wait(3)
        header = self.driver.find_element(
            by=By.CLASS_NAME, value="header-container")
        ps = header.find_elements(by=By.TAG_NAME, value="p")
        for p in ps:
            if (p.text == "로그인"):
                p.click()  # 로그인 다이얼로그
                self.driver.implicitly_wait(3)
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
                        btn.click()  # 로그인!

    def lets_crawl(self):
        try:
            self.login()
        except Exception as e:
            print("error in login", e)
            print(self.driver.get(self.entry_url))
            time.sleep(1)
            el = self.driver.find_element(by=By.TAG_NAME, value="body")
            print("el.text: ", el.text)
            raise e

        time.sleep(1)
        t_bar = tqdm(PROD_LIST_URLS)
        for i, obj in enumerate(t_bar):
            desc = f"{obj.part}, {obj.ctgr}, {obj.gender}, max_page: {obj.max_page}, idx: {i}"
            t_bar.set_description(desc=desc)
            print(desc)
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
                print(e)
                continue
            print("num of exist item: ", self.exist_cnt)
            print("num of new item: ", len(list(self.new_ids)))
        self.driver.close()
        self.driver.quit()
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
                    time.sleep(1)
                    vendorProdName = self.driver.find_element(
                        by=By.CSS_SELECTOR, value=".goods-detail-right p.title").text.strip()
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
                time.sleep(1)
            moreScroll = self.scrolling()
            time.sleep(1)
            if moreScroll == False or obj.max_page <= self.page:
                break

        return garments

    def scrolling(self) -> bool:
        scroll_pause_time = 1
        screen_height = self.driver.execute_script(
            "return window.screen.height;")
        # driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        self.driver.execute_script(
            "window.scrollTo(0, {screen_height});".format(screen_height=screen_height))
        time.sleep(scroll_pause_time)
        scroll_height = self.driver.execute_script(
            "return document.body.scrollHeight;")
        if ((screen_height) * self.page >= scroll_height) or self.page > 2:
            # 스롤 가능 높이보다 화면 높이가 높다면
            self.page = 1
            return False
        else:
            self.page += 1
            return True
