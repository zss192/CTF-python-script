#!/usr/bin/env python3
# CSDN刷访客
# Author: 夏日
# 分为指定url和遍历所有文章两种模式
# github: https://github.com/zss192/CTF-python-script/blob/master/shuaCsdn.py

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
    s = requests.Session()  # 创建session对象
    html = s.get(url, headers=header).text  # get请求获取全部文本
    title = re.compile(r'(?<=<h1 class="title-article" id="articleContentId">).*(?=<\/h1>)').findall(html)
    views = re.compile(r'(?<=<span class="read-count">).*(?=<\/span>)').findall(html)
    print("标题："+str(title)+str(views))

###
#指定文章访问
#times:遍历所有文章的次数
#space:每轮时间间隔(不要太快,经测试60最佳)
#urls:输入要刷的每个url，用逗号间隔，无数量限制
### 
def main(times,space,*urls):
    for i in range(1,times+1):
        print("第"+str(i)+"次请求 ")
        for url in urls:
            shua(url)
        time.sleep(space)

###
#遍历博客所有文章
#url:https://blog.csdn.net/zss192
#times:遍历所有文章的次数
#space:每篇文章访问间隔(不要太快只要保证第二轮访问间隔一分钟即可)
###     
def sumShua(url,times,space): 
    header={
            'User-Agent':random.choice(user_agent_list), 
            'Referer':random.choice(referer_list)
           }    
    s = requests.Session()  # 创建session对象
    html = s.get(url, headers=header).text  # get请求获取全部文本
    ls = re.findall(r""+url+"/article/details/\d*", html)
    ls = list(set(ls))
    for i in range(1,times+1):
        print("第"+str(i)+"次请求 ")
        for url in ls:
            shua(url)
            time.sleep(space)


#sumShua(url,times,space)
sumShua("https://blog.csdn.net/zss192",2,1)


#main(times,space,url...)
# main(150,65,
#     "https://blog.csdn.net/zss192/article/details/112388335",
#     "https://blog.csdn.net/zss192/article/details/112426855",
#     "https://blog.csdn.net/zss192/article/details/112388383",
#     "https://blog.csdn.net/zss192/article/details/112316516",
#     "https://blog.csdn.net/zss192/article/details/109095275",
#     "https://blog.csdn.net/zss192/article/details/109085435",
#     "https://blog.csdn.net/zss192/article/details/108694699",
#     "https://blog.csdn.net/zss192/article/details/109034551"
#   )


