# import requests
# import re
# import random
# import string

# url = 'https://ordinal-scale.hgame.n3ko.co/game.php'   # 链接
# s = requests.Session()	# 创建session对象
# html = s.get(url).text	# get请求, html保存请求的页面内容
# expression = re.compile(r'(?<=<div>).*(?=\=)').findall(html) #从html中匹配表达式（要计算的式子）?<=<div>表示开头是<div>
# payload = {'value': eval(expression[0])}	# eval计算式子(匹配出来的是列表所以用[0])并构造post请求的data部分
# flag = s.post(url, data=payload)	# post带参数提交
# flag.encoding = 'utf-8'	#'utf-8'格式
# print(flag.text)





import requests
import re
import random
import string

url = 'https://ordinal-scale.hgame.n3ko.co/game.php'  
s = requests.Session()	
html = s.get(url).text	
expression = re.compile(r'(?<=<div>).*(?=\=)').findall(html) 

payload = {'value': eval(expression[0])}	
flag = s.post(url, data=payload)	
flag.encoding = 'utf-8'	
print(flag.text)



'''
#配合php代码
phpText = requests.get('http://127.0.0.1:88/php%e8%84%9a%e6%9c%ac/rand.php')

#设置cookie、referer等
header  = {"Cookie":"PHPSESSID=294a9b966570ae34347a613e894d3271","Referer":"http://lab1.xseclab.com/pentest6_210deacdf09c9fe184d16c8f7288164f/index.php"}
flag = s.post(url, data=payload,headers=header)

'''

