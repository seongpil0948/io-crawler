from dataclasses import dataclass
import re
from lib.common.model import TBD


@dataclass
class SinsangGarment:
    createdAt: str  # isoformat
    updatedAt: str  # isoformat
    vendorProdId: str
    vendorProdPkgId: str
    vendorProdName: str  # 상품이름
    price_str: str
    vendorPrice: int
    titleImgs: list[str]
    bodyImgs: list[str]
    size: str
    color: str
    fabric: str
    info: str
    description: str
    gender: str
    part: str
    ctgr: str
    allowPending: bool
    stockCnt: int
    TBD: TBD
    prodType: str

    @property
    def is_valid(self):  # getter
        for v in self.__dict__.values():
            if isinstance(v, list) and len(list(filter(lambda x: len(x.strip()) > 0, v))) < 1:
                return False
            elif isinstance(v, str) and len(v) < 1:
                return False
        return True

    def setPrice(self):
        self.vendorPrice = int("".join(re.findall('[0-9]+',  self.price_str)))
