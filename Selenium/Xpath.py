import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#most used function

#syntax
//tagname[@attribute='value'] or //*[@attribute='value']
//*[@placeholder='First Name* ']

#text -> 
//label[text()='Full Name']

# contains -> 
//label[contains(text(), 'Full Name')]

# index -> 
//label[index]

# OR/AND -> 
//*[@placeholder='First Name' and @ng-model(jsut an example)="FirstName"]
//*[@placeholder='First Name' or @ng-model(jsut an example)="FirstName"]

# parent-child-ancestor
//form[@id='basicBootstrapForm']/child::div
//form[@id='basicBootstrapForm']//child::div #for nested childs
//form[@id='basicBootstrapForm']/parent::div
//form[@id='basicBootstrapForm']/ancestor::div

# following-sibling-preceding
//input[@id='checkbox1']//following-sibling::label
//input[@id='checkbox1']//preceding-sibling::label

time.sleep(60)

driver.quit()
