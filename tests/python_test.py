import os
test_email = os.environ.get('TEST_EMAIL')
test_password = os.environ.get('TEST_PASSWORD')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# import time

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1080",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=20).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

driver.get ("https://www.facebook.com")

# driver.find_element(By.ID, 'email').send_keys('fakeemail@crossbrowsertesting.com')
print(test_email)
driver.find_element(By.ID, 'email').send_keys(test_email)

# driver.find_element(By.ID, 'pass').send_keys('fakepassword1')
driver.find_element(By.ID, 'pass').send_keys(test_password)
print(test_password)

driver.find_element(By.NAME, 'login').click()

# driver.implicitly_wait(20)
# error_message = "Find your account and log in."
# get the errors (if there are)
errors = driver.find_elements(By.LINK_TEXT, "Find your account and log in.")
driver.get_screenshot_as_file("tests/Screen.png")


# # assert 'admin' not in driver.page_source

assert 'Invalid username or password' in driver.page_source
# print(driver.page_source)


# if any(error_message in e.text for e in errors):
#     print("Test PASSED. Login Failed")
# #     print(driver.title)
# #     print(driver.page_source)
# else:
#     print("Test Failed. Login successful")
# #     print(driver.title)
# #     print(driver.page_source)
driver.quit()
