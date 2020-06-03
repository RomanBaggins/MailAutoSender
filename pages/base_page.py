from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self): 
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_button_clickable(self, how, what, timeout=4):      
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))

    def did_url_chanched(self, what, timeout=4): 
        return WebDriverWait(self.browser, timeout).until(EC.url_contains((what)))

    



    #example: assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"   