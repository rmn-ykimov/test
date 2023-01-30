"""
This module tests the login functionality of Yandex Mail by testing different
scenarios for the username and password input fields.
The scenarios include providing valid credentials, invalid credentials, missing
username and missing password.
The test uses the pytest framework, Selenium WebDriver and the
expected_conditions module to interact with the browser and verify the result.

@pytest.mark.xfail: This test is expected to fail.
@pytest.mark.parametrize: This decorator is used to run the same test with
multiple sets of inputs, defined in the list of tuples.
browser_firefox: This is the fixture that provides the instance of the Firefox
browser.
YANDEX_URL: This is the URL of Yandex Mail.
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    """
    This function tests the login functionality of Yandex Mail by testing
    different scenarios for the username and password input fields.

    Arguments:
    browser_firefox: instance of the Firefox browser, provided by a fixture.
    username: the username to be entered in the login form.
    password: the password to be entered in the login form.
    expected_result: the expected result of the login action, can be either
    "Logged in successfully", "Invalid credentials", "Username is required", or
    "Password is required".

    The function opens the Yandex Mail URL, enters the username and password,
    submits the form, and verifies the result based on the expected result. If
    the result is "Logged in successfully", the function also logs out the
    account.
    """
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
