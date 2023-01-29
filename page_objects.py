from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
    def enter_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
        
    def click_login(self):
        self.driver.find_element(By.TAG_NAME, "button").click()

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        
    def search(self, query):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.submit()
        
    def get_results(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".g")