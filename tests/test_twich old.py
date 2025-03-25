# tests/1_test_twich.py
import sys
import os
import time
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
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
    
    # 用JavaScript 確保頁面已完全加載
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )
    
    # CSS 選擇器定位 search icon
    element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(2) > a:nth-child(2) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(1)"))
    )
    # 確保元素在視口中
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    # 點擊元素
    element.click()
    
    
    # 使用 CSS 選擇器定位輸入框
    search_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))
    )


    # 操作例如輸入搜索詞
    search_input.send_keys("StarCraft II")
    search_input.send_keys(Keys.RETURN)



    for _ in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    
        
    # # 等待搜索結果加載
    # WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "input.ScInputBase-sc-vu7u7d-0.ScInput-sc-19xfhag-0.gNGlOQ.bNTAcZ"))
    # )

    # 定位第一個頻道按鈕
    first_channel = driver.find_element(By.XPATH, "(//button[contains(@class, 'ScCoreLink-sc-16kq0mq-0')])[1]")
    
    # 滾動到元素可見
    driver.execute_script("arguments[0].scrollIntoView(true);", first_channel)
    # 嘗試點擊元素
    try:
        first_channel.click()
    except ElementClickInterceptedException:
        # 使用 JavaScript 點擊
        driver.execute_script("arguments[0].click();", first_channel)

# # 處理可能的彈窗（如登入提示或年齡確認）
#     try:
#         # 嘗試關閉登入提示
#         close_button = WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Dismiss')]")))
#         close_button.click()
#         print("已關閉登入提示")
#     except:
#         print("未偵測到登入提示")

# 首先等待頁面加載
    WebDriverWait(driver, 30).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

# 等待視頻元素存在
    video_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "video"))
    )

# # 處理可能的年齡限制按鈕
#     try:
#         mature_button = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ScCoreButton-sc-ocjdkq-0')]"))
#         )
#         mature_button.click()
#         print("已點擊年齡確認按鈕")
#     except:
#         print("未檢測到年齡確認按鈕")

# # 等待頁面上的加載動畫消失
#     try:
#         WebDriverWait(driver, 20).until_not(
#             EC.presence_of_element_located((By.CSS_SELECTOR, ".ScLoader-sc-1cz9ccu-0"))
#         )
#         print("加載動畫已消失")
#     except:
#         print("未檢測到加載動畫或超時")

    current_time = driver.execute_script("return document.querySelector('video').currentTime")
    time.sleep(2)
    new_time = driver.execute_script("return document.querySelector('video').currentTime")
    if new_time > current_time:
        driver.save_screenshot("streamer_page_screenshot.png")

