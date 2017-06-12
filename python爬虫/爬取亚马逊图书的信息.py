import requests

url = "https://www.amazon.cn/dp/B009FWYL04"

try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers=kv)#改写headers字段让电脑访问模拟浏览器访问网页
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[10000:20000])
except:
    print("ERROR")
