import pytest
from pages.login_page import LoginPage


ERROR_MESSAGE = ['Необходимо заполнить «Электронная почта».', 'Необходимо заполнить «Пароль».',
                 'Неверно указана электронная почта, логин или пароль.']


@pytest.mark.parametrize('message', ERROR_MESSAGE[:2])
def test_login_without_credetials(driver, message):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.click_submit_button()
    login_page.find_error_message(message)
    assert message in login_page.find_error_message(message)


@pytest.mark.parametrize('message', [ERROR_MESSAGE[1]])
def test_login_without_password(driver, message):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.enter_email("111")
    login_page.click_submit_button()
    login_page.find_error_message(message)
    assert message in login_page.find_error_message(message)


@pytest.mark.parametrize('message', [ERROR_MESSAGE[0]])
def test_login_without_password(driver, message):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.enter_password('lol')
    login_page.click_submit_button()
    login_page.find_error_message(message)
    assert message in login_page.find_error_message(message)


INAVALID_EMAIL = ['some_mail@.com', "1234@mail.com"]
INVALID_PSWD = ['10000†qwer0y']


@pytest.mark.parametrize('message', [ERROR_MESSAGE[2]])
@pytest.mark.parametrize('email', INAVALID_EMAIL)
@pytest.mark.parametrize('pswd', INVALID_PSWD)
def test_login_invalid_credentials(driver, message, email, pswd):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.enter_email(email)
    login_page.enter_password(pswd)
    login_page.click_submit_button()
    login_page.find_error_message(message)
    assert message in login_page.find_error_message(message)


VALID_EMAIL = ['User384']
VALID_PSWD = ['QlnNF0']
@pytest.mark.parametrize('email', VALID_EMAIL)
@pytest.mark.parametrize('pswd', VALID_PSWD)
def test_login_valid_credentials(driver, email, pswd):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.enter_email(email)
    login_page.enter_password(pswd)
    login_page.click_submit_button()
