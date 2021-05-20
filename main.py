import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"
r=requests.get(url)
htmlContent=r.content
# print(htmlContent)
soup=BeautifulSoup(htmlContent,'html.parser')

title =soup.title
# print(title)
# print(title.string)

para=soup.find_all('p')
# print(para)

anchors=soup.find_all('a')
# print(anc)

# print(soup.find('p'))#fist para

# print(soup.find('p')['class'])
# print(soup.find('p')['id'])

# print(soup.find_all('p',class_="lead"))#all para with class lead

# print(soup.find('p').get_text())
all_links=set()

for link in anchors:
    if(link.get('href') != '#'):
        linkText= "https://codewithharry.com" +link.get('href')
        # print(linkText)
        all_links.add(linkText)
print(all_links)
