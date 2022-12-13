import firebase_admin
from firebase_admin import firestore, credentials, get_app
from config import VENDOR_PROD_COLLECTION
from os import environ

credential_path = environ.get("CREDENTIAL_PATH")
assert credential_path is not None and len(credential_path) > 1
credential = credentials.Certificate(credential_path)
print("credential:", credential)
fire_app = firebase_admin.initialize_app(credential, name="fire_app")
print("fire_app: ", fire_app)


def exist_db_vendor_prod_ids():
    db = firestore.client(get_app(name="fire_app"))
    vendor_prod_collection = db.collection(VENDOR_PROD_COLLECTION)
    docs = vendor_prod_collection.stream()
    ids: set[str] = set()
    for doc in docs:
        doc_data = doc.to_dict()
        prod_id = doc_data.get("vendorProdPkgId", None)
        if prod_id is None:
            continue
        ids.add(prod_id)
    return ids
