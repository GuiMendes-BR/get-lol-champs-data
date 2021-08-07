from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base.base_element import BaseElement
from .base.base_page import BasePage
from .base.locator import Locator


class LeagueOfGraphs(BasePage):
    
    url = 'https://www.leagueofgraphs.com/champions/builds'

    def navigate_to_champ(self, name:str):
        self.driver.get(f"{self.url}/{name}")

    @property
    def champ_winrate(self):
        locator = Locator(by=By.XPATH, 
                            value="(//div[@class='pie-chart small'])[2]")
        return BaseElement(self.driver, locator).text

    def get_all_champs(self):
        xpath = '//div[@id="drop-champions"]//a[contains(@href, "/champions/builds/")]'

        soup = self.get_soup()
        div_with_all_champs = soup.find('div', id="drop-champions")

        list_of_champs = [champ.get_text().strip() for champ in div_with_all_champs.find_all('a')]

        list_of_champs = list_of_champs[1:] # Here we remove the first position because it's not a champion name
        return list_of_champs


