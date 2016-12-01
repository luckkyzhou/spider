# coding=utf-8
import requests

url = 'http://pjb.ecust.edu.cn/pingce/login.php'
data = {
    'action':'login',
    'sno':'10150982',
    'password':'125018'
}
r = requests.post(url,data=data)

fp = open('1.html','w+',encoding='utf-8')
fp.write(r.text)
fp.close()


