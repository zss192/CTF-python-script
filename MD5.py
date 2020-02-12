#MD5加密
import hashlib
def MD5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()

    
# print(MD5("abd"))
for i in range(9999999,9999999999):
	if(MD5(str(i))[:6]=="5ca419"):
		print(i)
		break


