from bs4 import BeautifulSoup #pip install BeautifulSoup4
import requests #pip install requests

# Enter a Keyword
keyword = input("Enter a Youtube Search Keyword:")

# Get the page
res = requests.get('https://www.youtube.com/results?search_query='+ keyword)

# Get the Body with lxml parser
bs = BeautifulSoup(res.text, 'lxml') #pip install lxml
# print(bs.text)

# get all elements with class 
ViewElements = bs.find_all('ul', class_='yt-lockup-meta-info')
print(ViewElements.text)
totalview = 0
for obj in ViewElements:
    lis = obj.findChildren()
    for li in lis:
        if li.string.endswith('views'):
            VideoViews = li.text.replace('views','').replace(',','')
            totalview = totalview + int(VideoViews)
            print(VideoViews)
print("------------------------------------------------------")
print("Total Views:"+ str(totalview))