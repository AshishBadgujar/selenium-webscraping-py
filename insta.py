from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib
import requests

username = input("enter instagram username:")

options = Options()
# options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://www.instagram.com/"+username+"/")

body = driver.find_element_by_tag_name('body')
page = body.get_attribute('innerHTML')

soup = BeautifulSoup(page, 'html.parser')
userimg = soup.select('img[alt="'+username+'\'s profile picture"]')

if not userimg:
    userimg = soup.select('.be6sR')

urllib.request.urlretrieve(userimg[0]["src"], 'userProfile.jpg')
driver.close()
