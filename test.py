import base64
import re
def shiZhuanAscii(ls):	#十进制列表转ascii
	flag=''
	for i in ls:
	    flag=flag+chr(int(i))
	return flag
def erZhuanShi(ls):		#二进制列表转十进制列表
	for i in range(len(ls)):
		ls[i]=int(ls[i],2)
	return ls
def splitS(s,n):	#把字符s每n个分到一个列表元素
	ls=re.findall('.{'+str(n)+'}', s)     #['1100110', '1101100']
	return ls

a='102 108 97 103 123 52 55 101 100 98 56 51 48 48 101 100 53 102 57 98 50 56 102 99 53 52 98 48 100 48 57 101 99 100 101 102 55 125'
a=a.split(' ')
print(shiZhuanAscii(a))

s="11001101101100"
print(splitS(s,2))

