from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators import selectors_profile as selector
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.login_url)

    def click_programs_button(self):
        self.find_element(selector.programs_button).click()

    def click_workouts_button(self):
        self.find_element(selector.work_button).click()

    def click_measurements_button(self):
        self.find_element(selector.measurement_button).click()

    def click_exercises_button(self):
        self.find_element(selector.exercises_button).click()

    def find_add_program(self):
        add_table = self.find_element(selector.table_text).text
        return add_table

    def find_your_wme(self):
        your_wme = self.find_element(selector.wme_text).text
        return your_wme

    def click_setting_button(self):
        self.find_element(selector.setting_button).click()

    def find_setting_button_text(self):
        setting_button_text = self.find_element(selector.setting_button).text
        return setting_button_text

    def click_my_programs_button(self):
        self.find_element(selector.my_programs_button).click()

    def enter_program_name(self, program_name: str):
        self.find_element(selector.program_name_field).send_keys(program_name)

    def enter_about_program_text(self, program_text: str):
        self.find_element(selector.program_text_field).send_keys(program_text)

    def click_add_new_program(self):
        self.find_element(selector.table_text).click()

    def click_save_button(self):
        self.find_element(selector.save_button).click()

    def find_program_setting_button(self):
        setting_button = self.find_element(selector.setting_program_button).is_displayed()
        return setting_button

    def find_alert_message(self):
        alert_message = self.find_element(selector.alert_message).text
        return alert_message

    def select_categories(self, value):
        select = Select(self.find_element(selector.combobox))
        select.select_by_value(value)

    def click_workout_button(self):
        self.find_element(selector.work_button).click()

    def click_add_new_day(self):
        self.find_element(selector.new_day_button).click()

    def find_created_new_day(self):
        new_day = self.find_element(selector.days_table).is_displayed()
        return new_day

    def click_delete_day(self):
        self.find_element(selector.delete_day_button).click()

    def check_delete_new_day(self):
        try:
            self.find_element(selector.days_table)
            return True
        except NoSuchElementException:
            return True

    def click_add_exercises_button(self):
        self.find_element((By.CSS_SELECTOR, '[class="hidden-xs"]')).click()

    def activate_check_box(self):
        self.find_element((By.CSS_SELECTOR, '[class="icheckbox_minimal-blue"]')).click()

    def click_save_exercise_button(self):
        self.find_element((By.CSS_SELECTOR, '[class="btn btn-primary"]')).click()

    def find_added_exercise(self):
        exercise = self.find_element((By.CSS_SELECTOR, '[class="exercise-info pull-left"]')).text
        return exercise

    def click_edit_button(self):
        self.find_element((By.XPATH, '//div[1]/div/a[2]/span')).click()

    def enter_exercise_name(self, exercise_name):
        self.find_element((By.XPATH, '//div/div/div/div[3]/div/div[1]/input[2]')).click()
        self.find_element((By.XPATH, '//div/div/div/div[3]/div/div[1]/input[2]')).send_keys(exercise_name)

    def click_save_edit_text(self):
        self.find_element((By.CSS_SELECTOR, '[class="btn btn-primary pull-right"]')).click()


    def find_exercise_name(self):
        ex_name = self.find_element((By.XPATH, '//div[1]/h3/span')).text
        return ex_name
