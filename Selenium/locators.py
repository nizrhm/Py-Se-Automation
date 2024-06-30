#Locators -> Locations of an object on the web-page
# DOM -> Direct/Document Object Model

"""
Locators: By.ID, By.NAME, By.CLASS_NAME, By.TAG_NAME, By.LINK_TEXT,
          By.PARTIAL_LINK_TEXT, By.CSS_SELECTOR, By.XPATH
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chr_options = Options()
chr_options.add_experimental_option("detach", True)
chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://demo.automationtesting.in/")

driver.implicitly_wait(5)

#By.ID
email_text = driver.find_element(By.ID, 'email')
email_text.send_keys("test@testy.com")
driver.find_element(By.ID, 'enterimg').click()

#By.LINK_TEXT - When you want to find something by it's name
#driver.get("https://google.com/")
#driver.find_element(By.LINK_TEXT, 'About').click()

#By.PARTIAL_LINK_TEXT - When you want to find something big by it's 
#name partial name(but name should be unique)
#driver.get("https://google.com/")
#driver.find_element(By.PARTIAL_LINK_TEXT, 'About').click()



time.sleep(60)

driver.quit()
