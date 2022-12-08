import pytest
from pages.profile_page import ProfilePage


def test_programs_button(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_programs_button()
    profile_page.find_add_program()
    assert "Добавить программу" in profile_page.find_add_program()


def test_workouts_button(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_workouts_button()
    profile_page.find_your_wme()
    assert 'Ваши тренировоки' in profile_page.find_your_wme()


def test_measurements_button(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_measurements_button()
    profile_page.find_your_wme()
    assert 'Ваши замеры' in profile_page.find_your_wme()


def test_exercises_button(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_exercises_button()
    profile_page.find_your_wme()
    assert 'Ваши упражнения' in profile_page.find_your_wme()


def test_setting_button(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_setting_button()
    profile_page.find_setting_button_text()
    assert 'Профиль' in profile_page.find_setting_button_text()


def test_create_new_program(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_my_programs_button()
    profile_page.click_add_new_program()
    profile_page.enter_program_name('lol')

    profile_page.click_save_button()
    profile_page.find_program_setting_button()
    assert profile_page.find_program_setting_button()


def test_create_new_program_without_name(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_my_programs_button()
    profile_page.click_add_new_program()
    profile_page.click_save_button()
    profile_page.find_alert_message()
