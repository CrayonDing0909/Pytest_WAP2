from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        by, value = locator
        return self.driver.find_element(by, value)
    
    def click(self, element):
        element.click()

    def type(self, element, text):
        element.send_keys(text)
