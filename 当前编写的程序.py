import requests
import re
from bs4 import BeautifulSoup

def Init_Dictionary(dic):
    #with open('D:\Python����ҵ\city_code.xml','r') as f: 
    with open('D:\��������Ա�����\Computer Language File\Python Language File\python����\Python����ҵ\city_code.xml','r') as f: 
        h=f.read()
    f.close()
    if isinstance(h,unicode):
        h=unicode(h,'utf-8')
    key=re.findall(r'<key>{1}(.*?)</key>{1}',h)
    value=re.findall(r'<string>{1}(.*?)</string>{1}',h)
    for i in range(len(key)):
        try:
            key1=key[i].encode('gb2312')
            value1=value[i].encode('gb2312')
            dic[key1]=value1
        except:
            continue
def main():
    dic={}
    Init_Dictionary(dic)
    print dic

main()
