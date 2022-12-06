from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = 'https://gymlog.ru/'
        self.login_url = 'https://gymlog.ru/profile/login/'
        self.actions = ActionChains(driver)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def scroll_page_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


