import pandas as pd
import requests
from bs4 import BeautifulSoup

# getting page data - created empty list 
product_name = []
Prices = []
description = []
reviews = []


url = "https://www.flipkart.com/search?q=mobile+under+20000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DMi&page=1"+str(1) 

r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text,"lxml")
box=soup.find("div", class_="_1YokD2 _3Mn1Gg")
# print(soup)
    
names = box.find_all("div", class_="_4rR01T")
# print(names)
for i in names:
        name = i.text
        product_name.append(name)
print (product_name)    
print (len(product_name))

# find prices/

prices = box.find_all("div", class_="_30jeq3 _1_WHN1")

for i in prices:
        name = i.text
        Prices.append(name)
print(Prices) 
print ("price -----",len(Prices))    

# description

desc = box.find_all("ul", class_="_1xgFaf")

for i in desc:
        name = i.text
        description.append(name)
print(description) 
print (len(description) ) 

# reviews


rev = box.find_all("div", class_="_3LWZlK")

for i in rev:
        name = i.text
        reviews.append(name)
print(reviews) 
print (len(reviews) ) 






    # while True:
# np=soup.find("a", class_ ="_1LKTO3").get("href")
#     # print(np)
# cnp="https://www.flipkart.com"+np
# print(cnp)

        # url = cnp
        # r = requests.get(url)
        # soup = BeautifulSoup(r.text,"lxml")