from dataclasses import dataclass
import time
from typing import Any


@dataclass
class IoUserInfo:
    createdAt: str
    updatedAt: str
    userId: str
    providerId: str
    userName: str
    displayName: str
    email: str
    emailVerified: bool
    profileImg: str | None
    role: str  # VENDOR
    fcmTokens: list
    passed: bool
    phone: str | None
    managerId: str | None
    workerIds: list[str]
    uncleId: str | None


@dataclass
class CompanyInfo:
    companyName: str
    companyNo: str
    companyCertificate: list[str]
    locations: list
    emailTax: str
    companyPhone: str
    shopLink: str
    ceoName: str
    ceoPhone: str
    managerName: str
    managerPhone: str


@dataclass
class VendorOperInfo:
    autoOrderApprove: bool
    saleManageType: str
    taxDeadlineDay: int
    expectNumProdMonthly: str


@dataclass
class IoUser:
    userInfo: IoUserInfo
    companyInfo: CompanyInfo
    operInfo: VendorOperInfo


def create_new_user(uid: str, email: str, user_name: str, curr_time: Any):
    email = f"{uid}@a.com"
    user_info = IoUserInfo(createdAt=curr_time, updatedAt=curr_time,
                           userId=uid, providerId="EMAIL",
                           userName=user_name, displayName=user_name, email=email,
                           emailVerified=False, profileImg=None, role="VENDOR",
                           fcmTokens=[], passed=True, phone=None, managerId=None, workerIds=[], uncleId=None)
    company_info = CompanyInfo(
        companyName=user_name, companyNo="", ceoName="",
        companyCertificate=[], locations=[],
        emailTax="", companyPhone="", shopLink="",
        ceoPhone="", managerName="", managerPhone="")
    oper_info = VendorOperInfo(
        autoOrderApprove=True, saleManageType="",
        taxDeadlineDay=10, expectNumProdMonthly="10~100")
    user = IoUser(userInfo=user_info,
                  companyInfo=company_info, operInfo=oper_info)
    return user
