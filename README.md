# Twitch WAP Automation Test Framework

## Project Structure
```
wap_test/
│── pages/
│   ├── base_page.py           # Base page operations (common functions)
│   ├── stream_page.py         # Streamer page (handling popups & screenshots)
│   ├── twitch_home_page.py    # Twitch main page (search operations)
│── test/
│   ├── test_twith.py          # Main function 
│── utils/
│   ├── __init__.py            
│   ├── helper.py
│   ├── WAP_browser_config.py  # WAP config(like mobile_emulation, Driver control...)         
│── README.md                  # Introduction to the test framework and execution
│── requirements.txt           # List of dependencies
Problem.json                   # For record problems when design the project and reference
```

## Please install requirements first by use command 
'pip -r install requirement.txt'


## User Scenario
1. go to https://m.twitch.tv/
2. click in the search icon.
3. input StarCraft II
4. scroll down 2 times 
5. Select one streamer 
6. on the streamer page wait until all is load and take a screenshot

## How to Run
1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the tests:
   ```bash
   pytest tests/test_twich.py
   ``` 
