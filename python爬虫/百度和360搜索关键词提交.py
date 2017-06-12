import requests
#http://www.baidu.com/s?wd=keyword  百度的关键词接口
#http://www.so.com/s?q=keyword  360的关键词接口
keyword = 'Python'
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s", params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("ERROR")

try:
    kv = {'q':keyword}
    r = requests.get("http://www.so.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("ERROR")
