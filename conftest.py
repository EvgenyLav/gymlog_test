from selenium import webdriver
import pytest
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage


@pytest.fixture(scope='session')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='session')
def authorization(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.enter_email('User384')
    login_page.enter_password('QlnNF0')
    login_page.click_check_box()
    login_page.click_submit_button()


@pytest.fixture(scope='function')
def create_new_day(driver):
    profile_page = ProfilePage(driver)
    profile_page.click_my_programs_button()
    profile_page.click_add_new_program()
    profile_page.enter_program_name('lol')
    profile_page.click_save_button()
    profile_page.click_workout_button()
    profile_page.click_add_new_day()
