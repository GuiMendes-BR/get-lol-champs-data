from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = "driver\chromedriver.exe"

class BasePage(object):
    
    url = None

    def __init__(self):
        options = self._get_driver_options()
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

    def go(self):
        self.driver.get(self.url)

    def _get_driver_options(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        return options