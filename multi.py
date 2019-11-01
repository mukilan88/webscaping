from urllib.request import urlopen
from bs4 import BeautifulSoup

file = "Details.csv"
f = open(file, "w")
Headers = "Name,Price,Rating\n"
f.write(Headers)
for page in range(0,1):
    url = "https://stackoverflow.com/users?page=1&tab=reputation&filter=week".format(page)
    html = urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    Title = soup.find_all("div", {"class":"user-details"})
    print(len(Title))
    
    for i in Title:
        try:
            name = i.find('a').get_text()
            print(name)
                        
            f.write("{}".format(name).replace(",","|")+ ",{}".format(price)+ ",{}".format(rating).replace(",", " ")+ "\n")
        except: AttributeError
f.close()