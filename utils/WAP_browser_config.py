# utils/WAP_browser_config.py   
from selenium import webdriver

def get_mobile_driver():
    mobile_emulation = {
        "deviceName": "Pixel 2"
    }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)
    return driver
