import json
import logging

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import LOGGER as SELENIUM_LOGGER

logger = logging.getLogger('server_logger')


class DriverFactory:

    SELENIUM_LOGGER.setLevel(logging.WARNING)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('/Users/ankita/Downloads/Interview/AccentureTask_p/test.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    @staticmethod
    def create_safari_driver():
        logger.info('Creating new [SafariBrowserDriver]')
        caps = webdriver.DesiredCapabilities.SAFARI.copy()
        caps['acceptInsecureCerts'] = True
        driver = webdriver.Chrome(desired_capabilities=caps)
        return driver

    @staticmethod
    def create_chrome_driver():
        logger.debug('Creating new [ChromeBrowserDriver]')
        path = f"--log-path=driver.log"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--kiosk")
        return webdriver.Chrome('/Users/ankita/Downloads/Interview/AccentureTask_p/chromedriver', options=chrome_options, service_args=["--verbose", path])

    @staticmethod
    def read_data(key):
        json_file = '/Users/ankita/Downloads/Interview/AccentureTask_p/inputData.json'
        with open(json_file) as json_file:
            json_data = json.load(json_file)
            for e in json_data:
                for k, v in e.items():
                    if key == k:
                        return v