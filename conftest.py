from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(scope='session')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def authorization(driver):
    driver.get('https://gymlog.ru/profile/login/')
    driver.find_element(By.CSS_SELECTOR, '[id=email]').send_keys('User384')
    driver.find_element(By.CSS_SELECTOR, '[id=password]').send_keys('QlnNF0')
    driver.find_element(By.XPATH, "//button").click()
