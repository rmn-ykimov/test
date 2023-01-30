"""
This module contains a functional test for searching on Google.

The test navigates to Google, enters a search query, submits the form,
locates the search results, and asserts that there are more than 10 results
and that one of the results contains the string "mvideo.ru".
"""
from config import GOOGLE_URL

def test_google_search(browser_firefox):
    """
    Function to test searching on Google using the browser_firefox object.

    Args:
    browser_firefox (obj): A Selenium webdriver object to interact with the
    browser

    Returns:
    None

    Raises:
    AssertionError: If the number of search results is not greater than 10 or
    if the search results do not contain the string "mvideo.ru"
    """
    # Navigate to Google URL
    browser_firefox.get(GOOGLE_URL)

    # Locate the search box
    search_box = browser_firefox.find_element_by_name("q")

    # Enter the search query into the search box
    search_box.send_keys("купить кофемашину bork c804")

    # Submit the form
    search_box.submit()

    # Locate the search results
    results = browser_firefox.find_elements_by_css_selector(".g")

    # Assert that there are more than 10 results
    assert len(results) > 10, f"Expected more than 10 results, but got {len(results)}"

    # Assert that the results contain the string "mvideo.ru"
    assert any("mvideo.ru" in result.text for result in results), "mvideo.ru not found in search results"
