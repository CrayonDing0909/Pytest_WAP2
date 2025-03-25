import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from utils.WAP_browser_config import get_mobile_driver
from utils.helper import screenshot
from page.twich_main_page import TwitchMainPage
from page.streamer_page import StreamerPage

@pytest.fixture
def driver():
    driver = get_mobile_driver()
    yield driver
    driver.quit()
    
def test_twitch_Scenario1(driver):
    Main_page = TwitchMainPage(driver)
    streamer_page = StreamerPage(driver)

    #Step
    Main_page.navigate_to()
    Main_page.click_search_icon()
    Main_page.enter_search_query("StarCraft II")
    Main_page.scroll_page()
    Main_page.select_streamer()   
    streamer_page.handle_popup()
    streamer_page.check_video_play_and_screenshot()