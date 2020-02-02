import re
import requests
import time

url = 'https://blog.csdn.net/zss192/article/details/104144885'   # 链接
for i in range(1,100):
	s = requests.Session()	# 创建session对象
	html = s.get(url).text	# get请求
	expression = re.compile(r'(?<=<span class="read-count">).*(?=<\/span>)').findall(html)
	print("第"+str(i)+"次请求 "+str(expression))
	time.sleep(30)