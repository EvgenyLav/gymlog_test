from pages.home_page import HomePage


def test_search_alert_message(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_programs_button()

