from .crawler import SinsangCrawler
from selenium.webdriver.remote.command import Command


def is_alive(driver):
    try:
        driver.execute(Command.STATUS)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    crawler = SinsangCrawler()
    crawler.log.info("init SinsangCrawler")
    try:
        crawler.lets_crawl()
    except Exception as e:
        crawler.log.error(f"occurred while {crawler.name} error: {e}")
        # if crawler.driver is not None and (is_alive(crawler.driver) is True or crawler.driver.session_id is not None):
        #     crawler.driver.close()
        #     crawler.driver.quit()
        raise e
    finally:
        crawler.dispose()
