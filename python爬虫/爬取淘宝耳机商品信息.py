import requests
url = "https://detail.tmall.com/item.htm?spm=a1z0d.6639537.1997196601.5.7BkulT&id=538332931706&skuId=3216636653526"
try:
    r = requests.get(url)
    r.raise_for_status()#访问出错时定义错误状态
    r.encoding = r.apparent_encoding
    print(r.text[:10000])
except:
    printf("ERROR")
