# pages/0-1_twich_main_page.py 
from page.base_page import BasePage
from selenium.webdriver.common.keys import Keys
class TwitchMainPage(BasePage):
    SEARCH_BUTTON = "//button[@aria-label='Search']"
    SEARCH_INPUT = "//input[@type='search']"
    SEARCH_RESULTS = "//div[@class='some-result-class']"
    def click_search(self):
        self.find(self.SEARCH_BUTTON).click()

    def enter_search_query(self, query):
        self.find(self.SEARCH_INPUT).send_keys(query)
        self.find(self.SEARCH_INPUT).send_keys(Keys.RETURN)

    def get_search_results(self):
        return self.find(self.SEARCH_RESULTS).text