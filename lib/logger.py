# https://jh-bk.tistory.com/40
# https://pypi.org/project/google-cloud-logging/
import logging as l
from os import environ
import google.cloud.logging as gcp_l
from google.cloud.logging_v2.handlers import CloudLoggingHandler
from google.oauth2 import service_account

credential_path = environ.get("CREDENTIAL_PATH")
assert credential_path is not None and len(credential_path) > 1


class IoLogger:
    def __init__(self, logger_name: str):
        self.logger_name = logger_name
        # self.file_path = file_path
        self.init_logger()
        self.add_handlers()
        self.log.info(f"init {logger_name}")

    def init_logger(self):
        # BUG: not working in named logging self.log = l.getLogger(name=logger_name)
        self.log = l.getLogger()
        self.log.setLevel(l.DEBUG)
        # if not os.path.exists(self.file_path):
        # os.makedirs(self.file_path)

    def add_handlers(self):
        self.log.addHandler(self.gcp_handler)
        # self.log.addHandler(self.file_handler)

    @property
    def formatter(self):
        return l.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    @property
    def gcp_handler(self):
        credentials = service_account.Credentials.from_service_account_file(
            credential_path)
        client = gcp_l.Client(credentials=credentials)
        handler = CloudLoggingHandler(
            client, name=self.logger_name, labels={"from": "python"})
        return handler

    # @property
    # def file_handler(self):
    #     handler = l.FileHandler(filename=self.file_path)
    #     handler.setFormatter(self.formatter)
    #     handler.setLevel(l.INFO)
    #     return handler
