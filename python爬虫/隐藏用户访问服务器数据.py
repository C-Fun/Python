import requests

pxs = { 'http' : 'http://user:pass@10.10.10.1:1234' }

r = requests.request('GET', 'http://www.bilibili.com', proxies=pxs)
