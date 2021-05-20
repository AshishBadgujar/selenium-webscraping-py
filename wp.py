from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()

driver.get("https://web.whatsapp.com/")

input("please scan qr code and press any key :")

Bh=driver.find_element_by_css_selector('span[title="Bhuvanesh"]')
Bh.click()

testinput=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

# time.sleep(2)
for i in range(10):
    testinput.send_keys("Hello !, message from web automation :)")
    testinput.send_keys(Keys.RETURN)