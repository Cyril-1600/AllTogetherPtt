import re
import requests
import urllib.parse
from html import unescape
from bs4 import BeautifulSoup

engine = "https://www.google.com/search"
searchPara = {"q":"寒流"} # google search搜尋參數字典化
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get(engine, params=searchPara, headers=headers) # headers參數為讓server以為我們的爬蟲程式一個瀏覽器的request。

if r.status_code == 200:
    r = urllib.parse.unquote(r.text) # decode url-coding的網址
    soup = BeautifulSoup(unescape(r), "html5lib")
    soup.encoding = "utf-8"
    #print(soup.prettify())

    items = soup.select('div.kCrYT > a[href]')
    for item in items:
        print("標題: " + item.text)
        url = item.get("href")
        url = url[7:]
        #print(url)
        p = re.compile("(https:.*)(&amp|&sa).*")
        url = re.search(p, url)
        print("連結: " + url.group(1) ) #取出p = re.compile("(https:.*)(&amp|&sa).*")括號內的第一群搜尋到的資料。
        print("\n")

else:
    print("Failed")