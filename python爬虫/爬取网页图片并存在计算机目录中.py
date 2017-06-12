#网络图片链接的格式
#http://www.example.com/picture.jpg
#国家地理中的一个图片
#http://www.nationalgeographic.com.cn/
#B站一副图片的地址
#http://i0.hdslb.com/bfs/drawyoo/99e9aa7cdab629ba8b5646b236ec992106d335c8.jpg
#P站的一副图片的地址
#http://i4.pixiv.net/img-original/img/2017/02/23/20/00/02/61601519_p0.jpg
import requests
import os
url = "http://i4.pixiv.net/img-original/img/2017/02/23/20/00/02/61601519_p0.jpg"
root = "D://计算机语言编译器//Computer Language File//Python Language File//python爬虫//Python爬虫图片//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("Saved picture successfully!")
    else:
        print("Picture existed!")
except:
    print("ERROR!")
