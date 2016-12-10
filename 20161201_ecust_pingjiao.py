# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re

def login(no,password): #登录函数
    url = 'http://pjb.ecust.edu.cn/pingce/login.php'
    data = {
        'action':'login',
        'password':password,
        'sno':no
    }
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded',
        'Referer':'http://pjb.ecust.edu.cn/pingce/index.php',
        'Origin':'http://pjb.ecust.edu.cn',
        'Host':'pjb.ecust.edu.cn',
    }
    rTwo = requests.post(url=url,data=data,headers=headers,allow_redirects=False)
    rOne = requests.post(url=url,data=data,headers=headers)
    list = [rOne.text,rTwo.cookies]
    return list

spiderFirst = re.findall('href="pg\.php+(.*?)"',login('10150982','125018')[0],re.S)
length = len(spiderFirst)
spiderFirstList = []
for i in range(0,length-1):
    spiderFirstList.append('http://pjb.ecust.edu.cn/pingce/pg.php'+spiderFirst[i])
    print("1")
print(spiderFirstList)

def getCookies(no,password):
    cookiesRaw = login(no,password)[1].items()[0]
    cookies = {
        'PHPSESSID': cookiesRaw[1]
    }
    return cookies

def pingCe():
    headers = {
        'Host':'pjb.ecust.edu.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8'
    }
    listOne = []
    for i in range(0,length-1):
        r = requests.get(url=spiderFirstList[i],headers=headers,cookies=getCookies('10150982','125018'))
        listOne.append(r.url)
    return listOne

a = pingCe()
print(a)

