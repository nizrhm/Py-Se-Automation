#Parent Window

parent = driver.current_window_handle
print(parent)

driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']").click()

#All Window

windows = driver.window_handles

#switch to child window

for win in windows:
    if win != parent:
        driver.switch_to.window(win)

#do action in child window

driver.find_element(By.XPATH, "//span[contains(text(),'Downloads')]").click()
driver.close()

driver.switch_to.window(parent)
driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']").click()

#Quit window

driver.quit()