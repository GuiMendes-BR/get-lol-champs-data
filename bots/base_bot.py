from abc import ABC, abstractmethod
from pages.base.base_page import BasePage

class BaseBot(ABC):

    @abstractmethod
    def run(self):
        # This method should always be implemented beacuse it will be used by the BotThread class
        pass