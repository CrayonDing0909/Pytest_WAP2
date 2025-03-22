# tests/1_test_twich.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils import WAP_browser_config
from page.twich_main_page import TwitchMainPage

@pytest.fixture
def driver():
    driver = WAP_browser_config.get_mobile_driver()
    yield driver
    driver.quit()

def test_search_twitch(driver):
    """測試 Twitch 搜尋功能"""
    twitch_home = TwitchMainPage(driver)
    twitch_home.open("https://m.twitch.tv/")
    
    # # 用JavaScript 確保頁面已完全加載
    # WebDriverWait(driver, 10).until(
    #     lambda d: d.execute_script('return document.readyState') == 'complete'
    # )
    
    # CSS 選擇器定位 search icon
    element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(2) > a:nth-child(2) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(1)"))
    )
    # 點擊元素
    element.click()
    
    # 使用 CSS 選擇器等待具有特定佔位符的輸入框可被點擊
    search_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#twilight-sticky-header-root > div > div > div > div > input"))
    )

    # 您可以在這裡添加更多操作，例如輸入搜索詞
    search_input.send_keys("StarCraft II")
    search_input.send_keys(Keys.RETURN)

     # 等待搜索結果加載
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.some-result-class"))  # 替換為實際的結果元素選擇器
    )
    
    # 在這裡可以添加斷言來驗證結果是否正確
    # 例如，檢查某個結果元素是否包含預期的文本
    result_text = driver.find_element(By.CSS_SELECTOR, "div.some-result-class").text
    assert "StarCraft II" in result_text

    # 停留在頁面上以查看結果
    input("Press Enter to continue...")  # 這行代碼會暫停測試，直到您按下 Enter 鍵

