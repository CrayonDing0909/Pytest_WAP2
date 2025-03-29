from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from page.base_page import BasePage
from utils.helper import screenshot
import time
from selenium.common.exceptions import TimeoutException
class StreamerPage(BasePage):
    VIDEO_PLAYER = (By.TAG_NAME, "video")
    LIVE_STREAM_TIME = (By.XPATH, "//span[@aria-label='Time Spent Live Streaming']")
    MATURE_POPUP_BUTTON = (By.CSS_SELECTOR, "button[data-a-target='content-classification-gate-overlay-start-watching-button']")
    # MATURE_POPUP_BUTTON = (By.XPATH, "//button[@data-a-target='content-classification-gate-overlay-start-watching-button']")
    #這邊試了一下css跟xpath用不同的方式取element,沒有感受到明顯差異

    def handle_popup(self):
        try:
            WebDriverWait(self.driver, 60).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            popup_button = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable(self.MATURE_POPUP_BUTTON)
            )
            self.click(popup_button)
            WebDriverWait(self.driver, 60).until(
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
            max_attempts = 5
            for attempt in range(max_attempts):
                paused = self.driver.execute_script("return arguments[0].paused;", video_element)
                if not paused:
                    current_time = self.driver.execute_script("return arguments[0].currentTime;", video_element)
                    time.sleep(2)
                    new_time = self.driver.execute_script("return arguments[0].currentTime;", video_element)
                    if new_time > current_time:
                        screenshot(self.driver, f"screenshot_{self.screenshot_count}")
                        self.screenshot_count += 1
                        return True
                else:
                    print(f"Attempt {attempt + 1}: Video paused or stopped.")
                time.sleep(5)
            if self.screenshot_count == 0:
                screenshot(self.driver, "final_state")
            return False
        except Exception as e:
            print(f"Error checking video playback: {e}")
            screenshot(self.driver, "error_state")
            return False


