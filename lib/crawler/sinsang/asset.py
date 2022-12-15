from dataclasses import dataclass


@dataclass
class ProdListObj:
    url: str
    part: str
    ctgr: str
    gender: str
    max_page: int = 1


PROD_LIST_URL_BASE = "https://sinsangmarket.kr/search"
PROD_LIST_URLS: list[ProdListObj] = [
    ProdListObj(
        # 여성의류 > 아우터
        url=PROD_LIST_URL_BASE + "?catItemId=1&catGenderId=1&catId=1",
        part="OUTER",
        ctgr="ETC",
        gender="FEMALE",
        max_page=5
    ),
    # ProdListObj(
    #     # 남성의류 > 아우터
    #     url=PROD_LIST_URL_BASE + "?catId=11&catItemId=1&catGenderId=2",
    #     part="OUTER",
    #     ctgr="ETC",
    #     gender="MALE"
    # ),
    ProdListObj(
        # 여성의류 > 티&탑
        url=PROD_LIST_URL_BASE + "?catItemId=1&catGenderId=1&catId=2",
        part="TOP",
        ctgr="ETC",
        gender="FEMALE",
        max_page=5
    ),
    # ProdListObj(
    #     # 남성의류 > 티&탑
    #     url=PROD_LIST_URL_BASE + "?catId=12&catItemId=1&catGenderId=2",
    #     part="TOP",
    #     ctgr="ETC",
    #     gender="MALE",
    #     max_page=2
    # ),
    ProdListObj(
        # 여성의류 > 원피스
        url=PROD_LIST_URL_BASE + "?catItemId=1&catGenderId=1&catId=3",
        part="DRESS",
        ctgr="ONE_PIECE",
        gender="FEMALE", max_page=5
    ),
    ProdListObj(
        # 여성의류 > 블라우스
        url=PROD_LIST_URL_BASE + "?catId=4&catItemId=1&catGenderId=1",
        part="TOP",
        ctgr="BLOUSE",
        gender="FEMALE", max_page=5
    ),
    ProdListObj(
        # 여성의류 > 니트
        url=PROD_LIST_URL_BASE + "?catId=5&catItemId=1&catGenderId=1",
        part="TOP",
        ctgr="KNIT",
        gender="FEMALE",
        max_page=5
    ),
    # ProdListObj(
    #     # 남성의류 > 니트
    #     url=PROD_LIST_URL_BASE + "?catId=14&catItemId=1&catGenderId=2",
    #     part="TOP",
    #     ctgr="KNIT",
    #     gender="MALE"
    # ),
    ProdListObj(
        # 여성의류 > 청바지
        url=PROD_LIST_URL_BASE + "?catId=6&catItemId=1&catGenderId=1",
        part="BOTTOM",
        ctgr="JEANS",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성의류 > 팬츠
        url=PROD_LIST_URL_BASE + "?catId=7&catItemId=1&catGenderId=1",
        part="BOTTOM",
        ctgr="PANTS",
        gender="FEMALE", max_page=5
    ),
    ProdListObj(
        # 여성의류 > 스커트
        url=PROD_LIST_URL_BASE + "?catId=8&catItemId=1&catGenderId=1",
        part="BOTTOM",
        ctgr="SKIRTS",
        gender="FEMALE", max_page=5
    ),
    ProdListObj(
        # 여성의류 > 셔츠/남방
        url=PROD_LIST_URL_BASE + "?catId=95&catItemId=1&catGenderId=1",
        part="TOP",
        ctgr="SHIRT",
        gender="FEMALE", max_page=5
    ),
    # ProdListObj(
    #     # 남성의류 > 셔츠/남방
    #     url=PROD_LIST_URL_BASE + "?catId=13&catItemId=1&catGenderId=2",
    #     part="TOP",
    #     ctgr="SHIRT",
    #     gender="MALE", max_page=2
    # ),
    ProdListObj(
        # 여성의류 > 세트
        url=PROD_LIST_URL_BASE + "?catId=94&catItemId=1&catGenderId=1",
        part="ETC",
        ctgr="TOP_BOTTOM_SET",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성의류 > 빅사이즈
        url=PROD_LIST_URL_BASE + "?catId=96&catItemId=1&catGenderId=1",
        part="ETC",
        ctgr="BIG_SIZE",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성의류 > 임부복
        url=PROD_LIST_URL_BASE + "?catId=97&catItemId=1&catGenderId=1",
        part="ETC",
        ctgr="MATERNITY",
        gender="FEMALE",
        max_page=5
    ),
    # ProdListObj(
    #     # 남성의류 > 수트
    #     url=PROD_LIST_URL_BASE + "?catId=15&catItemId=1&catGenderId=2",
    #     part="OUTER",
    #     ctgr="SUIT",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성의류 > 청바지
    #     url=PROD_LIST_URL_BASE + "?catId=16&catItemId=1&catGenderId=2",
    #     part="BOTTOM",
    #     ctgr="JEANS",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성의류 > 팬츠
    #     url=PROD_LIST_URL_BASE + "?catId=17&catItemId=1&catGenderId=2",
    #     part="BOTTOM",
    #     ctgr="PANTS",
    #     gender="MALE"
    # ),
    ProdListObj(
        # 여성 신발 > 로퍼/단화
        url=PROD_LIST_URL_BASE + "?catId=20&catItemId=2&catGenderId=1",
        part="SHOES",
        ctgr="LOAFERS",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성 신발 > 힐/펌프스
        url=PROD_LIST_URL_BASE + "?catId=21&catItemId=2&catGenderId=1",
        part="SHOES",
        ctgr="PUMPS",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성 신발 > 웨지힐
        url=PROD_LIST_URL_BASE + "?catId=22&catItemId=2&catGenderId=1",
        part="SHOES",
        ctgr="WEDGE_HEEL",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성 신발 > 샌들/슬리퍼
        url=PROD_LIST_URL_BASE + "?catId=23&catItemId=2&catGenderId=1",
        part="SHOES",
        ctgr="SLIPPERS",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성 신발 > 스니커즈/운동화
        url=PROD_LIST_URL_BASE + "?catId=24&catItemId=2&catGenderId=1",
        part="SHOES",
        ctgr="ATHLETIC",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성 신발 > 워커/부츠
        url=PROD_LIST_URL_BASE + "?catId=25&catItemId=2&catGenderId=1",
        part="SHOES",
        ctgr="BOOTS",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성 신발 > 수제화
        url=PROD_LIST_URL_BASE + "?catId=26&catItemId=2&catGenderId=1",
        part="SHOES",
        ctgr="HAND_MADE",
        gender="FEMALE",
        max_page=5
    ),
    # ProdListObj(
    #     # 남성 신발 > 로퍼/단화
    #     url=PROD_LIST_URL_BASE + "?catId=28&catItemId=2&catGenderId=2",
    #     part="SHOES",
    #     ctgr="LOAFERS",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 신발 > 스니커즈/운동화
    #     url=PROD_LIST_URL_BASE + "?catId=29&catItemId=2&catGenderId=2",
    #     part="SHOES",
    #     ctgr="ATHLETIC",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 신발 > 샌들/슬리퍼
    #     url=PROD_LIST_URL_BASE + "?catId=30&catItemId=2&catGenderId=2",
    #     part="SHOES",
    #     ctgr="SLIPPERS",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 신발 > 정장구두
    #     url=PROD_LIST_URL_BASE + "?catId=31&catItemId=2&catGenderId=2",
    #     part="SHOES",
    #     ctgr="DRESS",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 신발 > 수제화
    #     url=PROD_LIST_URL_BASE + "?catId=32&catItemId=2&catGenderId=2",
    #     part="SHOES",
    #     ctgr="HAND_MADE",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 신발 > 워커/부츠
    #     url=PROD_LIST_URL_BASE + "?catId=33&catItemId=2&catGenderId=2",
    #     part="SHOES",
    #     ctgr="BOOTS",
    #     gender="MALE"
    # ),
    ProdListObj(
        # 여성 가방 > 가죽
        url=PROD_LIST_URL_BASE + "?catId=45&catItemId=3&catGenderId=1",
        part="BAG",
        ctgr="LEATHER",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성 가방 > 숄더백
        url=PROD_LIST_URL_BASE + "?catId=46&catItemId=3&catGenderId=1",
        part="BAG",
        ctgr="SHOULDER",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성 가방 > 토트백
        url=PROD_LIST_URL_BASE + "?catId=47&catItemId=3&catGenderId=1",
        part="BAG",
        ctgr="TOD_BAG",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성 가방 > 크로스백
        url=PROD_LIST_URL_BASE + "?catId=48&catItemId=3&catGenderId=1",
        part="BAG",
        ctgr="CROSS",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성 가방 > 클러치/지갑
        url=PROD_LIST_URL_BASE + "?catId=49&catItemId=3&catGenderId=1",
        part="BAG",
        ctgr="CLUTCH",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성 가방 > 백팩
        url=PROD_LIST_URL_BASE + "?catId=50&catItemId=3&catGenderId=1",
        part="BAG",
        ctgr="BACKPACK",
        gender="FEMALE",
        max_page=5
    ),
    ProdListObj(
        # 여성 가방 > 기타
        url=PROD_LIST_URL_BASE + "?catId=51&catItemId=3&catGenderId=1",
        part="BAG",
        ctgr="ETC",
        gender="FEMALE",
        max_page=5
    ),
    # ProdListObj(
    #     # 남성 가방 > 숄더/토트백
    #     url=PROD_LIST_URL_BASE + "?catId=53&catItemId=3&catGenderId=2",
    #     part="BAG",
    #     ctgr="TOD_BAG",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 가방 > 크로스/메신저백
    #     url=PROD_LIST_URL_BASE + "?catId=54&catItemId=3&catGenderId=2",
    #     part="BAG",
    #     ctgr="CROSS",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 가방 > 백팩
    #     url=PROD_LIST_URL_BASE + "?catId=55&catItemId=3&catGenderId=2",
    #     part="BAG",
    #     ctgr="BACKPACK",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 가방 > 파우치
    #     url=PROD_LIST_URL_BASE + "?catId=56&catItemId=3&catGenderId=2",
    #     part="BAG",
    #     ctgr="CLUTCH",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 가방 > 지갑
    #     url=PROD_LIST_URL_BASE + "?catId=57&catItemId=3&catGenderId=2",
    #     part="BAG",
    #     ctgr="WALLET",
    #     gender="MALE"
    # ),
    ProdListObj(
        # 여성 악세사리 > 쥬얼리
        url=PROD_LIST_URL_BASE + "?catId=61&catItemId=4&catGenderId=1",
        part="ACCESSORY",
        ctgr="ETC",
        gender="FEMALE"
    ),
    ProdListObj(
        # 여성 악세사리 > 벨트
        url=PROD_LIST_URL_BASE + "?catId=62&catItemId=4&catGenderId=1",
        part="ACCESSORY",
        ctgr="BELT",
        gender="FEMALE"
    ),
    ProdListObj(
        # 여성 악세사리 > 밴드
        url=PROD_LIST_URL_BASE + "?catId=63&catItemId=4&catGenderId=1",
        part="ACCESSORY",
        ctgr="BAND",
        gender="FEMALE"
    ),
    ProdListObj(
        # 여성 악세사리 > 모자
        url=PROD_LIST_URL_BASE + "?catId=64&catItemId=4&catGenderId=1",
        part="HAT",
        ctgr="ETC",
        gender="FEMALE"
    ),
    ProdListObj(
        # 여성 악세사리 > 안경
        url=PROD_LIST_URL_BASE + "?catId=65&catItemId=4&catGenderId=1",
        part="ACCESSORY",
        ctgr="GLASSES",
        gender="FEMALE"
    ),
    ProdListObj(
        # 여성 악세사리 > 안경
        url=PROD_LIST_URL_BASE + "?catId=66&catItemId=4&catGenderId=1",
        part="ACCESSORY",
        ctgr="WATCH",
        gender="FEMALE"
    ),
    ProdListObj(
        # 여성 악세사리 > 기타
        url=PROD_LIST_URL_BASE + "?catId=67&catItemId=4&catGenderId=1",
        part="ACCESSORY",
        ctgr="ETC",
        gender="FEMALE"
    ),
    # ProdListObj(
    #     # 남성 악세사리 > 쥬얼리
    #     url=PROD_LIST_URL_BASE + "?catId=68&catItemId=4&catGenderId=2",
    #     part="ACCESSORY",
    #     ctgr="ETC",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 악세사리 > 모자
    #     url=PROD_LIST_URL_BASE + "?catId=69&catItemId=4&catGenderId=2",
    #     part="HAT",
    #     ctgr="ETC",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 악세사리 > 선글라스
    #     url=PROD_LIST_URL_BASE + "?catId=70&catItemId=4&catGenderId=2",
    #     part="ACCESSORY",
    #     ctgr="SUN_GLASSES",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 악세사리 > 안경
    #     url=PROD_LIST_URL_BASE + "?catId=71&catItemId=4&catGenderId=2",
    #     part="ACCESSORY",
    #     ctgr="GLASSES",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 악세사리 > 벨트
    #     url=PROD_LIST_URL_BASE + "?catId=72&catItemId=4&catGenderId=2",
    #     part="ACCESSORY",
    #     ctgr="BELT",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 악세사리 > 시계
    #     url=PROD_LIST_URL_BASE + "?catId=73&catItemId=4&catGenderId=2",
    #     part="ACCESSORY",
    #     ctgr="WATCH",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 남성 악세사리 > 기타
    #     url=PROD_LIST_URL_BASE + "?catId=74&catItemId=4&catGenderId=2",
    #     part="ACCESSORY",
    #     ctgr="ETC",
    #     gender="MALE"
    # ),
    # ProdListObj(
    #     # 유아 의류 > 아우터
    #     url=PROD_LIST_URL_BASE + "?catId=75&catItemId=1&catGenderId=4",
    #     part="OUTER",
    #     ctgr="ETC",
    #     gender="KIDS"
    # ),
    # ProdListObj(
    #     # 유아 의류 > 니트
    #     url=PROD_LIST_URL_BASE + "?catId=76&catItemId=1&catGenderId=4",
    #     part="TOP",
    #     ctgr="KNIT",
    #     gender="KIDS"
    # ),
    # ProdListObj(
    #     # 유아 의류 > 티/탑
    #     url=PROD_LIST_URL_BASE + "?catId=77&catItemId=1&catGenderId=4",
    #     part="TOP",
    #     ctgr="ETC",
    #     gender="KIDS"
    # ),
    # ProdListObj(
    #     # 유아 의류 > 청바지
    #     url=PROD_LIST_URL_BASE + "?catId=78&catItemId=1&catGenderId=4",
    #     part="BOTTOM",
    #     ctgr="JEANS",
    #     gender="KIDS"
    # ),
    # ProdListObj(
    #     # 유아 의류 > 원피스
    #     url=PROD_LIST_URL_BASE + "?catId=79&catItemId=1&catGenderId=4",
    #     part="DRESS",
    #     ctgr="ONE_PIECE",
    #     gender="KIDS"
    # ),
    # ProdListObj(
    #     # 유아 의류 > 팬츠
    #     url=PROD_LIST_URL_BASE + "?catId=80&catItemId=1&catGenderId=4",
    #     part="BOTTOM",
    #     ctgr="PANTS",
    #     gender="KIDS"
    # ),
    # ProdListObj(
    #     # 유아 의류 > 블라우스
    #     url=PROD_LIST_URL_BASE + "?catId=81&catItemId=1&catGenderId=4",
    #     part="TOP",
    #     ctgr="BLOUSE",
    #     gender="KIDS"
    # ),
    # ProdListObj(
    #     # 유아 의류 > 스커트
    #     url=PROD_LIST_URL_BASE + "?catId=82&catItemId=1&catGenderId=4",
    #     part="BOTTOM",
    #     ctgr="SKIRTS",
    #     gender="KIDS"
    # ),
    # ProdListObj(
    #     # 유아 의류 > 정장세트
    #     url=PROD_LIST_URL_BASE + "?catId=91&catItemId=1&catGenderId=4",
    #     part="ETC",
    #     ctgr="SUIT_SET",
    #     gender="KIDS"
    # ),
    # ProdListObj(
    #     # 유아 의류 > 상하세트
    #     url=PROD_LIST_URL_BASE + "?catId=98&catItemId=1&catGenderId=4",
    #     part="ETC",
    #     ctgr="TOP_BOTTOM_SET",
    #     gender="KIDS"
    # ),
]

if __name__ == "__main__":
    from collections import Counter
    urls = [obj.url for obj in PROD_LIST_URLS]
    url_cnt = Counter(urls)
    for url, cnt in url_cnt.items():
        if cnt > 1:
            print(f"중복 URL({cnt}) 발견!: {url}")
