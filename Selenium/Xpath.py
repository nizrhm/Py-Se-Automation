import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#most used function
#syntax
# //tagname[@attribute='value'] or //*[@attribute='value']

chr_options = Options()
chr_options.add_experimental_option("detach", True)
chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://demo.automationtesting.in/")

driver.implicitly_wait(5) #adds wait for page to be fully loaded

#By.ID
email_text = driver.find_element(By.ID, 'email')
email_text.send_keys("test@testy.com")
driver.find_element(By.ID, 'enterimg').click()

time.sleep(60)

driver.quit()
