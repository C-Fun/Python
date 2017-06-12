# -*- coding: cp936 -*-
import requests
from bs4 import BeautifulSoup
import bs4
import re
import os

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("ERROR In getHTMLText!")
        return ""

def getImageurl(html):
    string = ""
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all('img'):
        string += str(link.get('src'))
    return string
    
def parsePage(string):
    image_url = []
    image = re.findall(r'((http://i0.hdslb.com/bfs/drawyoo/){1}(.*?)(\.jpg){1})', string)
    for i in range(len(image)):
        image_url.append(image[i][0])
    return image_url

def GetPicture(image_url):
    root = "D://计算机语言编译器//Computer Language File//Python Language File//python爬虫//Python爬虫图片//"
    for i in range(len(image_url)):
        path = root + image_url[i].split('/')[-1]
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(image_url[i])
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close
                    print("Saved picture successfully!")
            else:
                print("Picture existed!")
        except:
            print("ERROR In GetPicture!")
            
def main():
    image_url = []
    html = ''
    url = "http://h.bilibili.com"
    html = getHTMLText(url)
    string = getImageurl(html)
    image_url = parsePage(string)
    GetPicture(image_url)
main()
