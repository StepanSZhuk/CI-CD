from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
display = Display(visible=0, size=(800, 800))  
display.start()



chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()

# Add your options as needed    
options = [
  # Define window size here
#    "--window-size=1200,1200",
   "--ignore-certificate-errors"
#    "--headless"
    #"--disable-gpu",
    #"--disable-extensions",
#    "--no-sandbox",
#    "--disable-dev-shm-usage",
#    '--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(options = chrome_options)

# driver.implicitly_wait(10)
# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

driver.get ("https://www.facebook.com")
driver.find_element(By.ID, 'email').send_keys('fakeemail@crossbrowsertesting.com')
# driver.implicitly_wait(10)

driver.find_element(By.ID, 'pass').send_keys('fakepassword1')
# driver.implicitly_wait(10)
# elem = driver.find_element(By.ID, 'pass')
# elem.send_keys('fakepassword1')
# elem.send_keys(Keys.RETURN)

# driver.find_element(By.ID, 'loginbutton').click()
driver.find_element(By.NAME, 'login').click()
# driver.implicitly_wait(20)

error_message = "Find your account and log in."
# get the errors (if there are)
errors = driver.find_elements(By.LINK_TEXT, "Find your account and log in.")

# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed

# assert 'admin' not in driver.page_source
print(driver.page_source)
assert 'Find your account and log in.' in driver.page_source


# if any(error_message in e.text for e in errors):
#     print("Test PASSED. Login Failed")
#     print(driver.title)
#     print(driver.page_source)
# else:
#     print("Test Failed. Login successful")
#     print(driver.title)
#     print(driver.page_source)
driver.quit()
