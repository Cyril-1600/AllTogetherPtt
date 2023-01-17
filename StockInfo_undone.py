import re
import requests
from bs4 import BeautifulSoup

url = "https://goodinfo.tw/StockInfo/StockDetail.asp?"
param = {"STOCK_ID":"2330"}
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, params=param, headers=header)
r.encoding = "utf-8"

if r.status_code == 200:
    soup = BeautifulSoup(r.text, "html.parser")
    print(soup.prettify())

