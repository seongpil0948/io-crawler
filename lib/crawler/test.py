# from ..logger import IoLogger
from lib.logger import IoLogger
import sys
sys.path.append("/Users/sp/Codes/Io/io-crawler")


class TestCrawler(IoLogger):
    entry_url: str
    name = "test-crawler"

    def __init__(self) -> None:
        super().__init__(self.name)
        self.log.info("info test crawler")
        self.log.info("info test crawler")
        self.log.warning("warn test crawler")
        self.log.error("error test crawler")


if __name__ == "__main__":
    t = TestCrawler()
    t.log.info("hi")
