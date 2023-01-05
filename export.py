
from tqdm import tqdm
from uuid import uuid5, NAMESPACE_DNS
from config import OUT_PATH, USER_COLLECTION, VENDOR_PROD_COLLECTION
from lib.crawler.sinsang.model import SinsangGarment
from lib.common.model import *
from lib.logger import IoLogger
from firebase_admin import firestore,  auth, get_app
from firebase_admin._auth_utils import UserNotFoundError
from dataclasses import asdict
import pickle
import os
import json
from datetime import datetime

MODULE_NAME = "export-crawl-result"
logger = IoLogger(logger_name=MODULE_NAME)


def export_vendor_prod(file_path: str):
    fire_app = get_app(name="fire_app")
    db = firestore.client(fire_app)
    with open(file=file_path, mode='rb') as f:
        crawl_data = pickle.load(f)
    f.close()

    garments: list[SinsangGarment] = crawl_data['garments']
    logger.log.info(f"{file_path} target garment length: {len(garments)}")
    lookup_ids: set[str] = crawl_data['lookup_ids']
    new_ids: set[str] = crawl_data['new_ids']
    vendor_prod_collection = db.collection(VENDOR_PROD_COLLECTION)

    # # update display
    # docs = vendor_prod_collection.stream()
    # for doc in docs:
    #     doc_data = doc.to_dict()
    #     pkg_id = doc_data.get("vendorProdPkgId", None)
    #     if pkg_id is None:
    #         continue

    #     tbd = doc_data.get("TBD", None)
    #     # 신상에서 가져온게 아니면 넘긴다
    #     if tbd is None or pkg_id is None or "from" not in tbd or tbd.get("from", "") != "SINSANG":
    #         continue
    #     # 발견됌에 따른 display 여부
    #     tbd["display_from"] = pkg_id in lookup_ids
    #     assert pkg_id not in new_ids, "새로운 데이터가 DB에 이미 데이터가 있습니다."
    #     vendor_prod_collection.document(doc_data.vendorProdId).update({
    #         u'TBD': tbd})

    user_collection = db.collection(USER_COLLECTION)
    # write new garments
    batch = db.batch()
    curr_time = datetime.now()
    set_cnt = 0
    for idx, g in tqdm(enumerate(garments)):
        # user create if not exist
        user_name = g.TBD.storeName
        uid = str(uuid5(NAMESPACE_DNS, user_name))
        email = f"{uid}@a.com"
        try:
            user = auth.get_user(uid, app=fire_app)
        except UserNotFoundError as e:
            user = auth.create_user(
                app=fire_app,
                uid=uid,
                email=email,
                email_verified=False,
                password='0525cc',
                display_name=user_name,
                disabled=False)

        doc_ref = user_collection.document(uid)
        doc = doc_ref.get()

        user = None
        if not doc.exists:
            new_user = asdict(create_new_user(
                uid, email, user_name, curr_time))
            doc_ref.set(new_user)
            user = new_user
        else:
            user = doc.to_dict()

        # product
        g.color = g.color.strip()
        g.size = g.size.strip()
        assert g.vendorProdPkgId in new_ids
        assert g.vendorProdPkgId in lookup_ids
        valid_id = str(uuid5(NAMESPACE_DNS, g.vendorProdPkgId +
                       g.vendorProdName+g.size+g.color))
        assert valid_id == g.vendorProdId, "vendor prod id validate error"
        # g.vendorProdId = valid_id
        g_doc_ref = vendor_prod_collection.document(g.vendorProdId)

        g_dict = asdict(g)
        g_dict["vendorId"] = user["userInfo"]["userId"]
        del g_dict["bodyImgs"]
        del g_dict["titleImgs"]
        doc = g_doc_ref.get()
        if not doc.exists:
            batch.set(g_doc_ref, g_dict)
            set_cnt += 1

        if idx % 100 == 0:
            batch.commit()
    batch.commit()
    return {"set_cnt": set_cnt, "total_cnt": idx + 1}


if __name__ == "__main__":
    logger.log.info(f"start {MODULE_NAME}")
    try:
        state_path = os.path.join(OUT_PATH, "state.json")
        if not os.path.exists(state_path):
            with open(state_path, "w", encoding="utf-8-sig") as f:
                json.dump({
                    "created_at": datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
                    "updated_at": datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
                    "done_files": []
                }, f, indent=4, sort_keys=True)

        with open(state_path, "r", encoding="utf-8-sig") as f:
            state = json.load(f)

        target_fs = []
        for f_name in os.listdir(OUT_PATH):
            if os.path.splitext(f_name)[1] == ".pkl" and f_name not in state["done_files"]:
                target_fs.append(f_name)
            else:
                logger.log.info(f"{f_name} is skipped export target")

        logger.log.info(f"target_files: {target_fs}")
        set_cnt = 0
        total_cnt = 0
        for target_file in target_fs:
            file_path = os.path.join(OUT_PATH, target_file)
            try:
                result = export_vendor_prod(file_path)
                set_cnt += result["set_cnt"]
                total_cnt += result["total_cnt"]
                logger.log.info(
                    f"processed {file_path} set_cnt: {result['set_cnt']}, total_cnt: {result['total_cnt']}")
            except Exception as e:
                logger.log.error(
                    f"occurred while export_vendor_prod file: {file_path} error: {e}")
                continue
            state["done_files"].append(target_file)
        logger.log.info(
            f"{MODULE_NAME} export done \n num of products: {total_cnt} \n num of new products: {set_cnt}")
        state["updated_at"] = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        with open(state_path, "w", encoding="utf-8-sig") as f:
            json.dump(state, f, indent=4, sort_keys=True)
    except Exception as e:
        logger.log.error(f"occurred while {MODULE_NAME} error: {e}")
        raise e
