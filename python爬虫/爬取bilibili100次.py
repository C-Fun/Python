import requests
import datetime

begin = datetime.datetime.now()
url = "http://www.bilibili.com"

for i in range(100+1):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(i)
    except:
        print("404NotFound!")

end = datetime.datetime.now()

print ("Endtime:", end - begin, "s")
