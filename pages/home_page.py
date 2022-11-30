from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators import selectors as selector


sign_in_button = (By.CLASS_NAME, 'login')

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_programs_button(self):
        self.find_element(selector.programs).click()

