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
driver.get("https://demo.automationtesting.in/Register.html")

driver.implicitly_wait(5)

#Radio Button
driver.find_element(By.XPATH, "//input[@value='Male']").click()

#checkbox and get attribute

li = driver.find_elements(By.XPATH, "//input[@type='checkbox]")

for ele in li:
    val = ele.get_attribute('value')
    print(val)
    if(val=='Cricket'):
        ele.click()


time.sleep(60)

driver.quit()


    