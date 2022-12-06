from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators import selector_login as selector
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.login_url)

    def click_submit_button(self):
        self.find_element(selector.submit_button).click()

    def find_error_message(self, message):
        wait = WebDriverWait(self.driver, 20)
        WebDriverWait(self.driver, 20)

        wait.until(EC.text_to_be_present_in_element(
            selector.loggin_error_message,
            message)
        )
        error_message_field = self.find_element(selector.loggin_error_message).text
        return error_message_field

    def enter_email(self, email: str):
        self.find_element(selector.email_field).send_keys(email)

    def enter_password(self, password: str):
        self.find_element(selector.password).send_keys(password)

    def click_check_box(self):
        self.find_element(selector.check_box).click()
