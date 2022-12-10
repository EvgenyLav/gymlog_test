from pages.home_page import HomePage
import allure

@allure.feature('Main Page')
def test_programs_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_programs_button()
    home_page.programs_page_test()
    assert "Программы тренировок" in home_page.programs_page_test()


@allure.feature('Main Page')
def test_exercises_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_exercises_button()
    assert home_page.cardio_exercises_button()


@allure.feature('Main Page')
def test_articles_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_articles_button()
    home_page.articles_page_text()
    assert 'Статьи на тему тренажерного зала' in home_page.articles_page_text()


@allure.feature('Main Page')
def test_news_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_news_button()
    home_page.news_page_text()
    assert 'Новости' in home_page.news_page_text()


@allure.feature('Main Page')
def test_contacts_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_contacts_button()
    home_page.contacts_email_filed()
    assert home_page.contacts_email_filed()


@allure.feature('Main Page')
def test_entered_only_contacts_email_field(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.scroll_page_to_bottom()
    home_page.enter_contacts_email_field("1@mil.ru")
    home_page.click_send_contact_message()
    home_page.find_error_message_no_text_in_contact_message_field()
    assert 'Необходимо заполнить «Сообщение».' in home_page.find_error_message_no_text_in_contact_message_field()


@allure.feature('Main Page')
def test_send_contact_message_with_clean_email_field(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.scroll_page_to_bottom()
    home_page.enter_contact_message_field('Привет, медвед!')
    home_page.click_send_contact_message()
    home_page.find_error_message_no_text_in_contact_email_field()
    assert 'Необходимо заполнить «Электронная почта».' in home_page.find_error_message_no_text_in_contact_email_field()


@allure.feature('Main Page')
def test_send_contacts_message_all_fields_clear(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.scroll_page_to_bottom()
    home_page.click_send_contact_message()
    home_page.find_error_message_all_filds_clear()
    err_message = "Необходимо заполнить «Электронная почта». Необходимо заполнить «Сообщение»."
    assert err_message in home_page.find_error_message_all_filds_clear()
