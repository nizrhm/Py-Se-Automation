import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chr_options = Options()
chr_options.add_experimental_option("detach", True)
chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window() #for maximizing the window pane

driver.implicitly_wait(5)

#Select class declaration with Webelement
Select_web = driver.find_element(By.ID, 'Skills')

sel = Select(Select_web)

#select by index
#sel.select_by_index(5)

#select by value
#sel.select_by_value('Configuration')

# select by visible text
#sel.selct_by_visible_text('Design')

#nagvigato different url
#driver.get('https://www.google.com/')

#back
#driver.back()

#refresh
#driver.refresh()

#forward
#driver.forward()

#current url
#print(driver.current_url())

driver.quit()