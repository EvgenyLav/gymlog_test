from pages.base_page import BasePage
from locators import selectors_home as selector
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_programs_button(self):
        self.find_element(selector.programs).click()

    def programs_page_test(self):
        page_text = self.find_element(selector.programs_page_text).text
        return page_text

    def click_exercises_button(self):
        self.find_element(selector.exercises).click()

    def cardio_exercises_button(self):
        cardio_button = self.find_element(selector.cardio).is_displayed()
        return cardio_button

    def click_articles_button(self):
        self.find_element(selector.articles_button).click()

    def articles_page_text(self):
        article_text = self.find_element(selector.articles_text).text
        return article_text

    def click_news_button(self):
        self.find_element(selector.news_button).click()

    def news_page_text(self):
        news_text = self.find_element(selector.news_text).text
        return news_text

    def click_contacts_button(self):
        self.find_element(selector.contacts_button).click()

    def contacts_email_filed(self):
        contacts_field = self.find_element(selector.contacts_email_field).is_displayed()
        return contacts_field

    def enter_contacts_email_field(self, email: str):
        self.find_element(selector.contacts_email_field).send_keys(email)

    def click_send_contact_message(self):
        self.find_element(selector.send_contact_message_button).click()

    def find_error_message_no_text_in_contact_message_field(self):
        wait = WebDriverWait(self.driver, 20)
        WebDriverWait(self.driver, 20)

        wait.until(EC.text_to_be_present_in_element(
            selector.error_contact_message_text, 'Необходимо заполнить «Сообщение»')
        )

        error_message_no_text_message_field = self.find_element(selector.error_contact_message_text).text
        return error_message_no_text_message_field

    def enter_contact_message_field(self, contact_message: str):
        self.find_element(selector.contact_message).send_keys(contact_message)

    def find_error_message_no_text_in_contact_email_field(self):
        wait = WebDriverWait(self.driver, 20)
        WebDriverWait(self.driver, 20)

        wait.until(EC.text_to_be_present_in_element(
            selector.error_contact_message_text, 'Необходимо заполнить «Электронная почта».')
        )

        error_message_no_text_message_field = self.find_element(selector.error_contact_message_text).text
        return error_message_no_text_message_field

    def find_error_message_all_filds_clear(self):
        wait = WebDriverWait(self.driver, 20)
        WebDriverWait(self.driver, 20)

        wait.until(EC.text_to_be_present_in_element(
            selector.error_contact_message_text,
            'Необходимо заполнить «Электронная почта». Необходимо заполнить «Сообщение».')
        )

        error_message_no_text_message_field = self.find_element(selector.error_contact_message_text).text
        return error_message_no_text_message_field
