# header file imported
from urllib.request import urlopen
from bs4 import BeautifulSoup

# creating a file name
file = "Details.csv"
f = open(file, "w") #open the file
Headers = "Name\n" #heading part
f.write(Headers) #inserting the heading

# loop for multi page open
for page in range(0,1):
    # opening the url
    url = "https://stackoverflow.com/users?page="+page+"&tab=reputation&filter=week".format(page)
    html = urlopen(url)
    # scraping using bs4
    soup = BeautifulSoup(html,"html.parser")
    # finding the name of the user inside the class file
    Title = soup.find_all("div", {"class":"user-details"})
    print(len(Title)) #total lenth of the user in the page
    
    # loop for getting the name 
    for i in Title:
        try:
            name = i.find('a').get_text()
            print(name)
            name_list = (name)
            f.write(name_list)
            f.write("\n")    
        except: AttributeError
f.close()