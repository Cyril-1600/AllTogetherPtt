import requests

res = requests.get("https://www.canva.com/design/DAENfMgsj-A/QtOWJQBJBJTXKZbgI9-YUQ/view?utm_content=DAENfMgsj-A&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu#5")

if res.status_code == 200: #回傳200表示有get到url資料
    print("Request get successfully")

if res.status_code == requests.codes.ok: #用200判斷外可以用requests.codes.ok代替
    print("Request get successfully")

#print(res.text) #將Get回傳的資料以text的形式呈現內容

#若url查詢內需要帶到參數的話就先建立字典當作參數帶入
my_params = {"key1": "value1", "key2": "value2"}
my_url = requests.get("http://httpbin.org/get", params=my_params)
print(my_url.url) #呈現出帶入參數後的url值
#雖然可以直接帶入，但因為編碼與格式問題，還是交由request整合

# 自訂表頭
my_headers = {"user-agent": "my-app/0.0.1"}
# 將自訂表頭加入GET請求中
my_url = requests.get("http://httpbin.org/get", headers=my_headers)
my_url2 = requests.get("http://httpbin.org/get")
print(my_url.url)
print(my_url2.url)

# Http帳號密碼登入
user_info = {"user", "passward"}
requests.get("http://httpbin.org/get", auth=user_info)
