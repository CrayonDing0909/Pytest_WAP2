from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from page.base_page import BasePage
from utils.helper import *
import time
from selenium.common.exceptions import TimeoutException
class StreamerPage(BasePage):
    VIDEO_PLAYER = (By.TAG_NAME, "video")
    LIVE_STREAM_TIME = (By.XPATH, "//span[@aria-label='Time Spent Live Streaming']")
    # MATURE_POPUP_BUTTON = (By.XPATH, "//button[@data-a-target='content-classification-gate-overlay-start-watching-button']")
    # MATURE_POPUP_CLOSE_BUTTON = (By.XPATH, "//button[@data-a-target='content-classification-gate-overlay-close-button']")
    # MATURE_POPUP_BUTTON = (By.XPATH, "//*[@id='channel-player-gate']/div/div/div[4]/div/button")
    # MATURE_POPUP_BUTTON = (By.XPATH, "//button[@data-a-target='content-classification-gate-overlay-start-watching-button']")
    MATURE_POPUP_BUTTON = (By.CSS_SELECTOR, "button[data-a-target='content-classification-gate-overlay-start-watching-button']")
    # MATURE_POPUP_BUTTON = (By.XPATH, "//button[@data-a-target='content-classification-gate-overlay-start-watching-button'][@class='ScCoreButton-sc-ocjdkq-0 hHbfNl']")
    #這邊要再多測一下Button的Xpath,不同的行為

    def handle_popup(self):
        try:
            WebDriverWait(self.driver, 30).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            popup_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.MATURE_POPUP_BUTTON)
            )
            self.click(popup_button)
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element(self.MATURE_POPUP_BUTTON)
            )
        except TimeoutException:
            pass


    def check_video_play_and_screenshot(self):
        try:
            WebDriverWait(self.driver, 30).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            video_element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(self.VIDEO_PLAYER)
            )
            self.screenshot_count = 0
            max_attempts = 6
            for attempt in range(max_attempts):
                paused = self.driver.execute_script("return arguments[0].paused;", video_element)
                if not paused:
                    current_time = self.driver.execute_script("return arguments[0].currentTime;", video_element)
                    time.sleep(2)
                    new_time = self.driver.execute_script("return arguments[0].currentTime;", video_element)
                    if new_time > current_time:
                        self.driver.save_screenshot(f"screenshot_{self.screenshot_count}.png")
                        self.screenshot_count += 1
                        return True
                else:
                    print(f"Attempt {attempt + 1}: Video paused or stopped.")
                time.sleep(5)
            if self.screenshot_count == 0:
                self.driver.save_screenshot("final_state.png")
                # print("Video failed to play after all attempts.")
            return False
        except Exception as e:
            print(f"Error checking video playback: {e}")
            self.driver.save_screenshot("error_state.png")
            return False






#     def check_video_play_and_screenshot(self):
# # 等待影片元素出現並可見
#         WebDriverWait(self.driver, 30).until(
#             lambda d: d.execute_script("return document.readyState") == "complete"
#         )
#         video_element = WebDriverWait(self.driver, 90).until(
#             EC.presence_of_element_located((By.TAG_NAME, "video"))        
#         )
#         screenshot_count = 0
#         max_attempts = 6  # 為了避免測試無限運行，限制最大嘗試次數
#         # 多次檢查影片是否播放
#         for _ in range(max_attempts):
#             # 檢查影片是否暫停
#             paused = self.driver.execute_script("return arguments[0].paused;", video_element)
#             if not paused:  # 如果影片沒有暫停
#                 # 檢查時間是否在增加
#                 current_time = self.driver.execute_script("return arguments[0].currentTime;", video_element)
#                 time.sleep(2)  # 等待 2 秒以確認時間變化
#                 new_time = self.driver.execute_script("return arguments[0].currentTime;", video_element)

#                 if new_time > current_time:  # 如果時間增加，影片正在播放
#                     self.driver.save_screenshot(f"screenshot_{screenshot_count}.png")
#                     screenshot_count += 1
#                     break
#             else:
#                 print("影片暫停或停止播放")

#             time.sleep(5)  # 每 5 秒檢查一次

#         # 如果沒有成功截圖，保存一張最終狀態的截圖
#         if self.screenshot_count == 0:
#             self.driver.save_screenshot("final_state.png")




    # def check_video_play_and_screenshot(self):

    #     WebDriverWait(self.driver, 30).until(
    #         lambda d: d.execute_script("return document.readyState") == "complete"
    #     )
    #     WebDriverWait(self.driver, 90).until(
    #         EC.presence_of_element_located(self.LIVE_STREAM_TIME)
    #     )
    #     current_time = self.driver.execute_script(self.LIVE_STREAM_TIME)
    #     time.sleep(2)
    #     new_time = self.driver.execute_script(self.LIVE_STREAM_TIME)
    #     if new_time > current_time:
    #         self.driver.save_screenshot("video_playback_screenshot.png")
    #     else:
    #         return False

