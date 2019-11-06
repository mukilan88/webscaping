# header file imported
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#  loop for multi page open
    # opening the url
url = "https://stackoverflow.com/users?page=2&tab=reputation&filter=week"
print(url)
html = requests.get(url)
print(html.text)
    # scraping using bs4
# soup = BeautifulSoup(html,'html5lib')
# print(soup)
    # finding the name of the user inside the class file
# for name in soup.find_all(class_='grid-layout--cell user-info  user-hover'):
#     try:
#         name_title = name.find(class_='user-details').getText()
#         print(name_title)
#     except: AttributeError
    
# Title = soup.select("#user-browser")
# for i in Title:
    # name = i.select_one('.user-details').getText()
    # print(name)
#total lenth of the user in the page
    

            
    