from bs4 import BeautifulSoup
import requests
import csv


url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=a303b35b-3f56-4f7a-b850-02fde4d8f648"

r = requests.get(url)
print(r.status_code)
# print(r.content)
# print(r.text[:500])

soup = BeautifulSoup(r.text, 'html5lib')
print(type(soup))
# Pull all text from the BodyText div
# main_list = soup.find(class_='_1HmYoV _35HD7C')
name_list = soup.find(class_='_3wU53n')
print(name_list.text)
price_list = soup.find(class_='_1vC4OE _2rQ-NK')
print(price_list.text)