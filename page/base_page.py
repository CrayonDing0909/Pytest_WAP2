    # pages/base_page_class.py
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element("xpath", locator)
