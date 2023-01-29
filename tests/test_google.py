from config import GOOGLE_URL

def test_google_search(browser_firefox):
    browser_firefox.get(GOOGLE_URL)

    search_box = browser_firefox.find_element_by_name("q")
    search_box.send_keys("buy a bork c804 coffee machine")
    search_box.submit()

    results = browser_firefox.find_elements_by_css_selector(".g")
    assert len(results) > 10, f"Expected more than 10 results, but got {len(results)}"
    assert any("mvideo.ru" in result.text for result in results), "mvideo.ru not found in search results"

#2. Write an autotest for Google search. The words “buy a bork c804 coffee machine” are entered into the search line, there are more than 10 results and mvideo.ru is present in the search results.
