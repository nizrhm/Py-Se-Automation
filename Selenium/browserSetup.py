import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#driver = webdriver.Chrome(Service = Service(ChromeDriverManager().install()))
chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())

# Create a Chrome webdriver instance
driver = webdriver.Chrome(service=chrome_service)

driver.get("https://www.bing.com/")

#keeps the window open for the set time in seconds
time.sleep(10)

# Close the browser
driver.quit()