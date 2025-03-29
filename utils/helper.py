import os
import time

def scroll_down(driver, times=1):
    for _ in range(times):
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(5)

def screenshot(driver, filename, count=None, base_dir="screenshots_from_twitch"):
    """
    Save a screenshot with a customizable filename and optional counter.
    
    :param driver: Selenium WebDriver instance
    :param filename: Base name for the screenshot file
    :param count: Optional counter for unique naming (e.g., screenshot_1.png)
    :param base_dir: Directory to store screenshots
    :return: Full path of the saved screenshot
    """
    os.makedirs(base_dir, exist_ok=True)
    if count is not None:
        full_filename = f"{filename}_{count}.png"
    else:
        full_filename = f"{filename}.png"
    full_path = os.path.join(base_dir, full_filename)
    driver.save_screenshot(full_path)
    return full_path