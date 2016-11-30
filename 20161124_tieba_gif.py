#coding = utf-8

import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import os

r = requests.get('http://tieba.baidu.com/p/3290408840')
html = r.text

fp = open("test.html",'w+')
fp.write(html)
fp.close()
soup = BeautifulSoup(open('test.html'))
gif = soup.find_all(pic_ext='gif')

myGif = re.findall('src="(.*?)"',str(gif),re.S)
fp = open("test.txt",'w+')
fp.write(str(myGif))
fp.close()

filePath = os.getcwd() + '\pythonImg'
os.chdir(filePath)
i = 1
for imgUrl in myGif:
    temp = filePath + '\%s.jpg' % i
    urllib.request.urlretrieve(imgUrl,temp)
    i+=1

print(os.getcwd())
os.rename('1.jpg','1.gif')

#count = 1
#for count in i:
#    jpgName = '\%s.jpg' % count
#    gifName = '\%s.gif' % count
#    os.rename(jpgName,gifName)
#    count+=1
