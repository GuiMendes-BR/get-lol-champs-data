from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

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
        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                            'notifications': 2, 'auto_select_certificate': 2,
                                                            'fullscreen': 2, 'disk-cache-size': 4096,
                                                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                            'media_stream_mic': 2, 'media_stream_camera': 2,
                                                            'protocol_handlers': 2,
                                                            'ppapi_broker': 2, 'automatic_downloads': 2,
                                                            'midi_sysex': 2,
                                                            'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                            'metro_switch_to_desktop': 2,
                                                            'protected_media_identifier': 2, 'app_banner': 2,
                                                            'site_engagement': 2,
                                                            'durable_storage': 2}}
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--no-sandbox')
        options.add_argument('log-level=3')
        options.Proxy = None
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        return options

    def close(self):
        self.driver.close()
        self.driver.quit()

    def get_soup(self) -> BeautifulSoup:
        return BeautifulSoup(self.driver.page_source, 'lxml')