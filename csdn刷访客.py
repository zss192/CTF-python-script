import re
import requests
import time
import random

user_agent_list=[
            'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
            'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
            'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
            'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',  
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36' 
        ]
referer_list=[
            'https://blog.csdn.net/zss192/article/details/104144885',
            'http://blog.csdn.net/',
            'https://blog.csdn.net/zss192',
            'https://blog.csdn.net/zss192/article/details/104144006'
        ]

def shua(url):
	header={
			'User-Agent':random.choice(user_agent_list), 
     		'Referer':random.choice(referer_list)
       	   }	
	s = requests.Session()	# 创建session对象
	html = s.get(url, headers=header).text	# get请求获取全部文本
	title = re.compile(r'(?<=<h1 class="title-article">).*(?=<\/h1>)').findall(html)
	views = re.compile(r'(?<=<span class="read-count">).*(?=<\/span>)').findall(html)
	print("标题："+str(title)+str(views))

def main(times,space,*urls):
	for i in range(1,times+1):
		print("第"+str(i)+"次请求 ")
		for url in urls:
			shua(url)
		time.sleep(space)


times=100       #刷访客次数
space=60		#每次访问间隔时间
main(times,space,
	# "https://blog.csdn.net/zss192/article/details/104144885",
	# "https://blog.csdn.net/zss192/article/details/104144006",
	"https://blog.csdn.net/zss192/article/details/104133448"
	)









