import re
import os
import requests
import webbrowser
from bs4 import BeautifulSoup
import sys

def AllTogetherSpider(inputPage):
    list = []
    reg = re.compile(".*上頁.*")
    pre_page = ""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    latest_url = "https://www.ptt.cc/bbs/AllTogether/index.html"
    r = requests.get(latest_url, headers=headers)
    if r.status_code == 200:
        btfSoup = BeautifulSoup(r.text, "html.parser")
        #print(btfSoup.prettify())
        select_res = btfSoup.select("a", div="btn-group btn-group-paging")
        for i in select_res:
            if re.match(reg, i.text):
                #print(i.get("href"))
                pre_page = i.get("href")

    reg_num = re.compile("/bbs/AllTogether/index(.*).html")
    num = int(re.search(reg_num, pre_page).group(1)) + 1
    #print(num)

    #print("--------------------------------")

    reg = re.compile(".*(徵男).*")
    # pre_page_num = input("輸入AllTogether.ptt往前幾頁貼文\n")
    pre_page_num = inputPage
    for i in range(num, num - int(pre_page_num), -1):
        url = "https://www.ptt.cc/bbs/AllTogether/index" + str(i) + ".html"
        #print(url)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            #print(soup.prettify())
            res = soup.select("div.title > a[href]")
            for i in res:
                if re.match(reg, i.text):
                    # print("標題: " + i.text)
                    title = "標題: " + i.text
                    # title_list.append(title)
                    url2 = "https://www.ptt.cc" + i.get("href")
                    # print("連結: " + url2)
                    # url_list.append(url2)
                    webbrowser.open(url2)
                else:
                    continue

    # os.system("pause")


if __name__ == "__main__":
    AllTogetherSpider()