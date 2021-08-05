  
from selenium.webdriver.common.by import By

from .base.base_element import BaseElement
from .base.base_page import BasePage
from .base.locator import Locator


class LeagueOfGraphs(BasePage):
    
    url = 'https://www.leagueofgraphs.com/champions/builds'

    def _navigate_to_champ(self, name:str):
        self.driver.get(f"{self.url}/{name}")

    @property
    def _champ_winrate(self):
        locator = Locator(by=By.XPATH, 
                            value="(//div[@class='pie-chart small'])[2]")
        return BaseElement(self.driver, locator).text

    def get_champ_data(self, name):

        self._navigate_to_champ(name=name)
        return{'winrate': self._champ_winrate}