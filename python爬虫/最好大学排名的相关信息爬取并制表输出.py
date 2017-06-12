# -*- coding: gb2312 -*-

import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r= requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print "ERROR"
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:^10}\t{2:^10}\t{3:^10}"
    print tplt.format("排名", "大学名称", "所在省份", "得分")
    for i in range(num):
        u = ulist[i]
        u0 = u[0].encode('gb2312')
        u1 = u[1].encode('gb2312')
        u2 = u[2].encode('gb2312')
        u3 = u[3].encode('gb2312')
        print tplt.format(u0, u1, u2, u3)                                 

def main():
    unifo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(unifo, html)
    printUnivList(unifo, 20) #20 Universities
main()
