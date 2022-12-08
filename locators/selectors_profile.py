from selenium.webdriver.common.by import By

programs_button = (By.CSS_SELECTOR, '[class="small-box bg-red"]')
workout_button = (By.CSS_SELECTOR, '[class="small-box bg-yellow"]')
measurement_button = (By.CSS_SELECTOR, '[class="small-box bg-aqua"]')
exercises_button = (By.CSS_SELECTOR, '[class="small-box bg-green"]')
table_text = (By.CSS_SELECTOR, '[class="btn btn-success pull-right"]')
wme_text = (By.CSS_SELECTOR, '[class="content-header"]')
setting_button = (By.CSS_SELECTOR, '[class="btn btn-primary btn-block"]')
my_programs_button = (By.XPATH, '//*[@id="solar"]//li[3]/a')
save_button = (By.XPATH, '//button')
program_name_field = (By.ID, 'field_name_u')
setting_program_button = (By.XPATH, '//*[@id="edit-program"]//ul/li[1]/a')
alert_message = (By.XPATH, '//*[@id="object-form"]/div/div[1]/div[2]')