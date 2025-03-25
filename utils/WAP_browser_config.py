# utils/WAP_browser_config.py   
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #可以自動下載跟管理driver,不用手動,CICD好幫手
from webdriver_manager.chrome import ChromeDriverManager


def get_mobile_driver():
    mobile_emulation = {
        "deviceName": "iPhone X"
    }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver
