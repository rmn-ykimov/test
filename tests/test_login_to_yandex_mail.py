import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from config import YANDEX_URL

@pytest.mark.xfail
@pytest.mark.parametrize("username, password, expected_result", [
    ("valid_user1", "valid_password1", "Logged in successfully"),
    ("valid_user2", "valid_password2", "Logged in successfully"),
    ("invalid_user", "invalid_password", "Invalid credentials"),
    ("missing_user", "valid_password", "Username is required"),
    ("valid_user", "missing_password", "Password is required")
])
def test_login_to_yandex_mail(browser_firefox, username, password, expected_result):
    browser_firefox.get(YANDEX_URL)
    # enter username and password
    username_input = browser_firefox.find_element_by_id("passp-field-login")
    password_input = browser_firefox.find_element_by_id("passp-field-passwd")
    login = browser_firefox.find_element_by_id("passp:sign-in")

    username_input.send_keys(username)
    login.click()
    password_input.send_keys(password)

    # submit the form
    login_button = browser_firefox.find_element_by_tag_name("button")
    login_button.click()

    # check the expected result
    if expected_result == "Logged in successfully":
        wait = WebDriverWait(browser_firefox, 10)
        inbox_title = wait.until(EC.presence_of_element_located((By.ID, "nb-1")))
        assert "Входящие" in inbox_title.text
        
        # logout the account
        logout_link = browser_firefox.find_element_by_link_text("Logout")
        logout_link.click()
    else:
        assert expected_result in browser_firefox.page_source




#1. Write an autotest to enter the mailbox on www.yandex.ru.