import pytest
import allure
from pages.profile_page import ProfilePage


VALUES = ['1', '2', '3', '8']

@allure.feature('Profile page')
@pytest.mark.profile_page
def test_programs_button(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_programs_button()
    profile_page.find_add_program()
    assert "Добавить программу" in profile_page.find_add_program()


@allure.feature('Profile page')
@pytest.mark.profile_page
def test_workouts_button(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_workouts_button()
    profile_page.find_your_wme()
    assert 'Ваши тренировоки' in profile_page.find_your_wme()


@allure.feature('Profile page')
@pytest.mark.profile_page
def test_measurements_button(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_measurements_button()
    profile_page.find_your_wme()
    assert 'Ваши замеры' in profile_page.find_your_wme()


@allure.feature('Profile page')
@pytest.mark.profile_page
def test_exercises_button(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_exercises_button()
    profile_page.find_your_wme()
    assert 'Ваши упражнения' in profile_page.find_your_wme()


@allure.feature('Profile page')
@pytest.mark.profile_page
def test_setting_button(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_setting_button()
    profile_page.find_setting_button_text()
    assert 'Профиль' in profile_page.find_setting_button_text()


@allure.feature('My programs')
@pytest.mark.my_programs
@pytest.mark.parametrize('value', VALUES)
def test_create_new_program(driver, value, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_my_programs_button()
    profile_page.click_add_new_program()
    profile_page.enter_program_name('lol')
    profile_page.enter_about_program_text("Some text")
    profile_page.select_categories(value)
    profile_page.click_save_button()
    profile_page.find_program_setting_button()
    assert profile_page.find_program_setting_button()


@allure.feature('My programs')
@pytest.mark.my_programs
def test_create_new_program_without_name(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_my_programs_button()
    profile_page.click_add_new_program()
    profile_page.click_save_button()
    profile_page.find_alert_message()
    assert "Необходимо заполнить «Название»." in profile_page.find_alert_message()


@allure.feature('My programs')
@pytest.mark.my_programs
def test_add_new_day(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_my_programs_button()
    profile_page.click_add_new_program()
    profile_page.enter_program_name('lol')
    profile_page.click_save_button()
    profile_page.click_workout_button()
    profile_page.click_add_new_day()
    profile_page.find_created_new_day()
    assert profile_page.find_created_new_day()


@allure.feature('My programs')
@pytest.mark.my_programs
def test_delete_day(driver, authorization, create_new_day):
    profile_page = ProfilePage(driver)
    profile_page.click_delete_day()
    profile_page.accept_alert_messages()
    profile_page.check_delete_new_day()
    assert profile_page.check_delete_new_day()


@allure.feature('My programs')
@pytest.mark.my_programs
def test_add_exercise(driver, authorization, create_new_day):
    profile_page = ProfilePage(driver)
    profile_page.click_add_exercises_button()
    profile_page.activate_check_box()
    profile_page.click_save_exercise_button()
    profile_page.find_added_exercise()
    assert "Бег на беговой дорожке" in profile_page.find_added_exercise()


@allure.feature('My programs')
@pytest.mark.my_programs
def test_edit_exercise(driver, authorization, create_new_day):
    profile_page = ProfilePage(driver)
    profile_page.click_edit_button()
    profile_page.enter_exercise_name("name")
    profile_page.click_edit_button()
    profile_page.find_exercise_name()
    profile_page.find_exercise_name()
    assert "name" in profile_page.find_exercise_name()


@allure.feature('My workouts')
@pytest.mark.my_workouts
def test_add_workout(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_my_workouts_button()
    profile_page.click_add_new_workout()
    profile_page.click_save_new_workout()
    profile_page.find_workout()
    assert profile_page.find_workout()


@allure.feature('My programs')
@pytest.mark.my_workouts
def test_delete_workout(driver, authorization):
    profile_page = ProfilePage(driver)
    profile_page.click_my_workouts_button()
    profile_page.click_add_new_workout()
    profile_page.click_save_new_workout()
    profile_page.click_delete_workout()
    profile_page.accept_alert_messages()
    profile_page.check_delete_workout()
    assert profile_page.check_delete_workout()








