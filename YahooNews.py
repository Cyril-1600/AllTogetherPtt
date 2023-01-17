import re
import requests
from bs4 import BeautifulSoup

r = requests.get("https://tw.yahoo.com/")

if r.status_code == 200:
    soup = BeautifulSoup(r.text, "html5lib")
    #print(soup.prettify())

    stories = soup.find_all("a", class_="active_V(v)")
    for i in stories:
        #print(i)
        #print(i.string)
        #print(i.text)
        #新聞標題
        print("標題: " + i.text)
        #新聞網址
        print("網址: " + i.get("href"))
        print("\n")
else:
    print("Failed")
