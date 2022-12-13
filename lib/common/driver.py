from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.chrome.service import Service as ChromeService
from os import environ


class RemoteWrap(webdriver.Remote):
    def quit(self) -> None:
        super().quit(self)
        self.session_id = None


def get_driver():
    # # https://peter.sh/experiments/chromium-command-line-switches/
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--disable-gpu')
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-application-cache')
    options.add_argument('--no-sandbox')
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--incognito")
    options.add_argument("test-type=browser")
    # options.add_argument('headless')  # 서버측에서 확인 가능..
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1280")
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    if environ.get('SELENIUM_URL') is not None:
        selenium_url = environ.get('SELENIUM_URL')
        driver = webdriver.Remote(command_executor=selenium_url,
                                  desired_capabilities=DesiredCapabilities.CHROME, options=options)
        return driver
        # return RemoteWrap(selenium_url, DesiredCapabilities.CHROME)
    else:
        raise Exception(
            'No remote Selenium webdriver provided in the environment.')
    # service = ChromeService(executable_path=ChromeDriverManager().install())

    # driver = webdriver.Chrome(service=service, options=options)
    # driver.set_window_size(1920, 1280)
    # return driver
