from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import BasePage
from utils.helper import scroll_down
from selenium.webdriver.common.keys import Keys

class TwitchMainPage(BasePage):
    SEARCH_BUTTON = (By.XPATH, "/html/body/div[1]/div[2]/a[2]/div/div[1]")
    SEARCH_INPUT = (By.XPATH, '//*[@id="twilight-sticky-header-root"]/div/div/div/div/input')
    STREAMER_LINK = (By.XPATH, '//*[@id="page-main-content-wrapper"]/div/div/section[1]/div[2]/button')
    
    def navigate_to(self):
        self.driver.get("https://www.twitch.tv")
        # self.driver.get("https://m.twitch.tv/videos/2413162329") #popup page
        WebDriverWait(self.driver, 30).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    
    def click_search_icon(self):
        search_button = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        self.click(search_button)

    def enter_search_query(self, query):
        search_input = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(self.SEARCH_INPUT)
        )
        self.click(search_input)
        self.type(search_input, query)
        search_input.send_keys(Keys.RETURN)

    def scroll_page(self):
        scroll_down(self.driver, 2)

    def select_streamer(self):
        streamer = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(self.STREAMER_LINK)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", streamer)
        self.driver.execute_script("arguments[0].click();", streamer)