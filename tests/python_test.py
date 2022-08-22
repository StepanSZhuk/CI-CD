# pip install selenium
# pip install webdriver_manager
# pip install chromedriver-autoinstaller
# from asyncio.windows_events import NULL
# from contextlib import nullcontext
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path
# service = Service(executable_path=ChromeDriverManager().install())

# driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
from selenium.webdriver.chrome.options import Options as ChromeOptions
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.headless = True
# command_executor = "http://localhost:4444/wd/hub"
# driver = webdriver.Remote(command_executor, desired_capabilities=options.to_capabilities())
# driver.get("https://google.com")
# options = ChromeOptions()
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title

# downloading chromedriver to the test path from https://chromedriver.storage.googleapis.com/index.html?path=104.0.5112.79/
# driver = webdriver.Chrome("C:/Users/Stepan_Zhuk/Documents/GitHub/reporting/test/chromedriver.exe")

# driver.get("http://selenium.dev")
# driver.get("https://192.168.59.100:32008")




driver.get ("https://www.facebook.com")
# driver.find_element(By.ID, 'email').send_keys('fakeemail@crossbrowsertesting.com')

# driver.find_element(By.ID, 'pass').send_keys('fakepassword1')

# # driver.find_element(By.ID, 'loginbutton').click()
# d = driver.find_element(By.NAME, 'login').click()

# # wait the ready state to be complete
# WebDriverWait(driver=driver, timeout=10).until(
#     lambda x: x.execute_script("return document.readyState === 'complete'")
# )
# error_message = "Find your account and log in."
# # get the errors (if there are)
# errors = driver.find_elements(By.LINK_TEXT, "Find your account and log in.")

# # print the errors optionally
# # for e in errors:
# #     print(e.text)
# # if we find that error message within errors, then login is failed
# if any(error_message in e.text for e in errors):
#     print("Test PASSED. Login Failed")
# else:
#     print("Test Failed. Login successful")

driver.quit()
