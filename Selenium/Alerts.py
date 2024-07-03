#Alerts
#Types-> Simple, Confirmation, Content.

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
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

driver.find_element(By.ID, 'OKTab').click()

driver.implicitly_wait(5)

time.sleep(2)

driver.switch_to.alert.accept()

driver.find_element(By.XPATH,"//a[@href='#CancelTab]").click()
time.sleep(2)

driver.switch_to.alert.dismiss()

driver.find_element(By.XPATH, "//a[@href='#Textbox']").click()
time.sleep(2)

tx=driver.switch_to.alert.text
print(tx)

driver.switch_to.send_keys("Test")
driver.switch_to.alert.dismiss()
driver.quit()