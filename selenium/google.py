from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://google.com")
print(driver.title)
driver.find_element(By.NAME, "q").send_keys("codewithharry")
optionList = driver.find_elements_by_css_selector('ul.erkvQe li span')
print(len(optionList))
for ele in optionList:
    print(ele.text)
    if ele.text == "codewithharry youtube":
        ele.click()
        break
time.sleep(5)
driver.quit()
