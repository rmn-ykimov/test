import pytest
from selenium import webdriver

@pytest.fixture
def browser_firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
    
@pytest.fixture
def browser_chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def credentials():
    YANDEX_USERNAME = "your_username"
    YANDEX_PASSWORD = "your_password"
    return YANDEX_USERNAME, YANDEX_PASSWORD
