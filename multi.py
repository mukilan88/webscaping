# header file imported
from urllib.request import urlopen
from bs4 import BeautifulSoup

# creating a file name
file = "Details.csv"
f = open(file, "w") #open the file
Headers = "Name,Location\n" #heading part
f.write(Headers) #inserting the heading

range = [10, 20, 30]
# loop for multi page open

for i in range:
    print(i)
    # opening the url
    url = "https://stackoverflow.com/users?page=()&tab=reputation&filter=week".format(i)
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
            location = i.find('span', class_ ='user-location')
            print(name)
            # print(locatin)
            name_list = (name)
            # location_list = (location)
            f.write(name_list)
            # f.write(location_list)
            f.write("\n")    
        except: AttributeError
f.close()