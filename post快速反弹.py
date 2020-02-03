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



import re
import requests
import time

url = 'https://blog.csdn.net/qq_20817327/article/details/77739962'   # 链接
s = requests.Session()	# 创建session对象
html = s.get(url).text	# get请求
expression = re.compile(r'(?<=<span class="read-count">).*(?=<\/span>)').findall(html)
print(html)




