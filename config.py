import os

VENDOR_PROD_COLLECTION = u"vendorProduct"
USER_COLLECTION = u"user"
OUT_PATH = os.path.join(os.getcwd(), "out")
if not os.path.exists(OUT_PATH):
    os.makedirs(OUT_PATH)