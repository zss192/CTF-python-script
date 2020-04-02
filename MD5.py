#MD5加密
import hashlib
def MD5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()

#215962017  if ($md5==md5($md5)) 
# for i in range(999999999999):
# 	y=True
# 	a=MD5("0e"+str(i))
# 	b=a[2:]
# 	if(a[:2]=="0e"):
# 		for x in b:
# 			if(ord(x)>=97 and ord(x)<=102):
# 				y=False
# 				continue
# 		if(y):
# 			print(i)
# 			break


# print(MD5("abd"))
# for i in range(9999999,9999999999):
# 	if(MD5(str(i))[:6]=="5ca419"):
# 		print(i)
# 		break