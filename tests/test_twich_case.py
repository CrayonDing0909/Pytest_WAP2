# # tests/1_test_twich.py
# import sys
# import os
# import time
# import pytest
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import ElementClickInterceptedException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from utils import WAP_browser_config
# from page.twich_main_page import TwitchMainPage

# @pytest.fixture
# def driver():
#     driver = WAP_browser_config.get_mobile_driver()
#     yield driver
#     driver.quit()

# def test_open_twitch_home(driver):
#     """打開 Twitch 主頁"""
#     twitch_home = TwitchMainPage(driver)
#     twitch_home.open("https://m.twitch.tv/")
#     WebDriverWait(driver, 10).until(
#         lambda d: d.execute_script('return document.readyState') == 'complete'
#     )

# def test_search_function(driver):
#     """搜尋功能"""
#     test_open_twitch_home(driver)
#     element = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(2) > a:nth-child(2) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(1)"))
#     )
#     driver.execute_script("arguments[0].scrollIntoView(true);", element)
#     element.click()
#     search_input = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))
#     )
#     search_input.send_keys("StarCraft II")
#     search_input.send_keys(Keys.RETURN)

# def test_scroll_and_click_channel(driver):
#     """測試滾動並點擊頻道"""
#     test_search_function(driver)
#     for _ in range(2):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)
#     first_channel = driver.find_element(By.XPATH, "(//button[contains(@class, 'ScCoreLink-sc-16kq0mq-0')])[1]")
#     driver.execute_script("arguments[0].scrollIntoView(true);", first_channel)
#     try:
#         first_channel.click()
#     except ElementClickInterceptedException:
#         driver.execute_script("arguments[0].click();", first_channel)

# def test_video_playback(driver):
#     """影片播放"""
#     test_scroll_and_click_channel(driver)
#     WebDriverWait(driver, 30).until(
#         lambda d: d.execute_script("return document.readyState") == "complete"
#     )
#     video_element = WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located((By.TAG_NAME, "video"))
#     )
    
#     # # 檢查年齡確認按鈕點擊
#     # try:
#     #     mature_button = WebDriverWait(driver, 5).until(
#     #         EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ScCoreButton-sc-ocjdkq-0')]"))
#     #     )
#     #     mature_button.click()
#     # except:
#     #     pass 
    

#     screenshot_count = 0
#     max_attempts = 6  
    
#     for _ in range(max_attempts):
#         paused = driver.execute_script("return document.querySelector('video').paused;")
#         if not paused:

#             current_time = driver.execute_script("return document.querySelector('video').currentTime;")
#             time.sleep(2)  
#             new_time = driver.execute_script("return document.querySelector('video').currentTime;")
            
#             if new_time > current_time: 
#                 driver.save_screenshot(f"screenshot_{screenshot_count}.png")
#                 screenshot_count += 1
#                 break  
#         else:
#             print("failed")
        
#         time.sleep(5) 
    
#     if screenshot_count == 0:
#         driver.save_screenshot("final_state.png")



