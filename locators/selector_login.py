from selenium.webdriver.common.by import By

submit_button = (By.XPATH, "//button")
loggin_error_message = (By.CSS_SELECTOR, "[class='alert result alert-danger']")
email_field = (By.CSS_SELECTOR, '[id=email]')
password = (By.CSS_SELECTOR, '[id=password]')
check_box = (By.CSS_SELECTOR, '[class="icheckbox_minimal-blue checked"]')