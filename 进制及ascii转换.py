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
	ls=re.findall('.{'+str(n)+'}', s)     
	return ls

#示例：
'''
s="110011011011001100001110011111110111010111011000010101110101010110011011101011101110110111011110011111101"
ls=splitS(s,7)  #['1100110', '1101100', '1100001', '1100111', '1111011', '1010111', '0110000', '1010111', '0101010', '1100110', '1110101', '1101110', '1101110', '1111001', '1111101']
ls=erZhuanShi(ls)  #[102, 108, 97, 103, 123, 87, 48, 87, 42, 102, 117, 110, 110, 121, 125]
ls=shiZhuanAscii(ls) #flag{W0W*funny}
print(ls)
'''



