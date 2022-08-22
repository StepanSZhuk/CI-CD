# pip install selenium
# pip install webdriver_manager
# pip install chromedriver-autoinstaller
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path
# service = Service(executable_path=ChromeDriverManager().install())

# driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))


from selenium.webdriver.chrome.options import Options as ChromeOptions
service = ChromeService(executable_path=ChromeDriverManager().install())
options = selenium.webdriver.ChromeOptions()
# options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
# # options.add_argument("--remote-debugging-port=9222")
options.headless = True
driver = selenium.webdriver.Chrome(service=service, options=options)
# # command_executor = "http://localhost:4444/wd/hub"
# # driver = webdriver.Remote(command_executor, desired_capabilities=options.to_capabilities())
# # driver.get("https://google.com")
# # options = ChromeOptions()
# driver = webdriver.Chrome(options=options)


driver.get ("https://www.facebook.com")
driver.find_element(By.ID, 'email').send_keys('fakeemail@crossbrowsertesting.com')

driver.find_element(By.ID, 'pass').send_keys('fakepassword1')

# driver.find_element(By.ID, 'loginbutton').click()
d = driver.find_element(By.NAME, 'login').click()

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Find your account and log in."
# get the errors (if there are)
errors = driver.find_elements(By.LINK_TEXT, "Find your account and log in.")

# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("Test PASSED. Login Failed")
else:
    print("Test Failed. Login successful")

driver.quit()
