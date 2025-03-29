# Twitch WAP Automation Test Framework

## Overview
This project is a Web Automation Platform (WAP) designed to test Twitch's mobile website (`https://m.twitch.tv/`) using Selenium with pytest as the test runner. The framework emphasizes scalability, maintainability, and modularity, making it a foundation for testing web applications efficiently.

### Demo: Test Running Locally
![Test Demo](https://github.com/CrayonDing0909/Pytest_WAP2/blob/main/Pytest_demo.gif)
![Test Demo Popup](https://github.com/CrayonDing0909/Pytest_WAP2/blob/main/Pytest_popup_case.gif)

## Framework Design Principles
- **Modularity**: Pages are separated into individual classes (e.g., `TwitchMainPage`, `StreamerPage`) using the Page Object Model (POM) for better code reuse and maintenance.
- **Scalability**: New pages or test scenarios can be added by extending `BasePage` or creating new test files under `tests/`.
- **Maintainability**: Common utilities (e.g., scrolling, screenshot) are centralized in `utils/`, and browser configurations (e.g., mobile emulation) are isolated in `WAP_browser_config.py`.
- **Robustness**: Handles dynamic elements like popups with explicit waits and flexible locators.


## Project Structure
wap_test/
├── pages/                    # Page Object Model classes
│   ├── base_page.py          # Base class with common Selenium operations (e.g., click, find)
│   ├── streamer_page.py      # Streamer page logic (e.g., popup handling, video checks)
│   ├── twitch_home_page.py   # Twitch homepage logic (e.g., search, navigation)
├── tests/                    # Test cases
│   ├── test_twitch.py        # Test scenarios for Twitch mobile site
├── utils/                    # Utility modules
│   ├── init.py               # Empty init file
│   ├── helper.py             # Helper functions (e.g., scroll_down, screenshot)
│   ├── WAP_browser_config.py # Browser setup with Chrome Mobile Emulator
├── README.md                 # Framework introduction and instructions
├── requirements.txt          # Python dependencies
├── Problem.json              # Log of design challenges and solutions

## Prerequisites
- Python 3.9+
- Chrome browser and compatible ChromeDriver
- Dependencies listed in `requirements.txt`

## Installation
1. Clone the repository:
   git clone https://github.com/CrayonDing0909/Pytest_WAP2.git
2. Install dependencies:
   pip install -r requirements.txt

## User Scenario
1. Navigate to https://m.twitch.tv/ using Chrome Mobile Emulator.
2. Click the search icon.
3. Input "StarCraft II" in the search field.
4. Scroll down the page twice.
5. Select a streamer
6. On the streamer page, handle any popup (e.g., mature content warning), wait for the video to load, and take a screenshot.
Note: The framework automatically handles popups that may appear before video playback, ensuring robust test execution.

## How to Run
1. Ensure ChromeDriver is in your PATH or configured in WAP_browser_config.py.
2. Run the tests:
   pytest tests/test_twitch.py -v

## Mobile Emulation
The framework uses Chrome's Mobile Emulator (configured in `WAP_browser_config.py`) to simulate a mobile device
