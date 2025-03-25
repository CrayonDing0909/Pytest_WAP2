from selenium.webdriver.common.action_chains import ActionChains
import time
import os

def scroll_down(driver, times=1):
    for _ in range(times):
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(5)

def screenshot(driver, filename):
    os.makedirs("screenshots_from_twith_streamer", exist_ok=True)
    driver.save_screenshot(f"screenshots_from_twith_streamer/{filename}.png")