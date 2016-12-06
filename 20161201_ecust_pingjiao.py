# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
def login(no,password):
    url = 'http://pjb.ecust.edu.cn/pingce/login.php'
    data = {
        'action':'login',
        'password':password,
        'sno':no
    }
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip,deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded',
        'Referer':'http://pjb.ecust.edu.cn/pingce/index.php',
        'Origin':'http://pjb.ecust.edu.cn',
        'Proxy-Connection':'keep-alive',
        'Host':'pjb.ecust.edu.cn',
        'Upgrade-Insecure-Requests':'1',
        'Cache-Control':'max-age=0',
        'Content-Length':'41'
    }
    r = requests.post(url=url,data=data,headers=headers)
    list = [r.text,r.cookies]
    return list
print(login('10150982','125018')[1])
spiderFirst = re.findall('href="pg\.php+(.*?)"',login('10150982','125018')[0],re.S)
length = len(spiderFirst)
spiderFirstList = []
for i in range(0,length-1):
    spiderFirstList.append('http://pjb.ecust.edu.cn/pingce/pg.php'+spiderFirst[i])
print(spiderFirstList)

url = str(spiderFirstList[0])
headers = {
    'Host':'pjb.ecust.edu.cn',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip,deflate',
    'Accept-Language':'zh-CN,zh;q=0.8'
}
cookies = {
    'PHPSESSID':'j5coiqqk6n380gq46khucp2ea5'
}
r = requests.get(url=url,headers=headers,cookies=cookies)
fp = open('2.html','w+',encoding='utf-8')
fp.write(r.text)
fp.close()