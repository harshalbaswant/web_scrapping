import pandas
import requests
from bs4 import BeautifulSoup
for i in range(2,10):
    url = "https://www.flipkart.com/search?q=mobile+under+20000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DMi&page="+str(i) 

    r = requests.get(url)
    print(r)
    soup = BeautifulSoup(r.text,"lxml")
    # print(soup)
    # next_page

    # while True:
    np=soup.find("a", class_ ="_1LKTO3").get("href")
    # print(np)
    cnp="https://www.flipkart.com"+np
    print(cnp)

        # url = cnp
        # r = requests.get(url)
        # soup = BeautifulSoup(r.text,"lxml")