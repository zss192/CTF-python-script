import re
import requests
import time

def shua(url):
	s = requests.Session()	# 创建session对象
	html = s.get(url).text	# get请求获取全部文本
	title = re.compile(r'(?<=<h1 class="title-article">).*(?=<\/h1>)').findall(html)
	views = re.compile(r'(?<=<span class="read-count">).*(?=<\/span>)').findall(html)
	print("标题："+str(title)+str(views))

def main(space,*urls):
	for i in range(1,5):
		print("第"+str(i)+"次请求 ")
		for url in urls:
			shua(url)
		time.sleep(space)

space=60	#每次访问间隔时间
main(space,
	"https://blog.csdn.net/zss192/article/details/104144885",
	"https://blog.csdn.net/zss192/article/details/104144006",
	"https://blog.csdn.net/zss192/article/details/104133448"
	)



