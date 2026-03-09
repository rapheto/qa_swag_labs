import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    prefs = {
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver_instance = webdriver.Chrome(options=chrome_options)
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()