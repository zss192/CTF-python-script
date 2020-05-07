#MD5加密
import hashlib
def MD5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()
a="1%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%93%D0w%C9Ur%C1%89y+u%EB%A3c%28%D4Z%CF%E8%0E%F1%B9%5D%D4%FBy%7C%5D%8F%B2A%C6%02%AC%C0%09X%E6%5C%EC%E79b%824fko%00%06%2C%1F%03%8F%AD%91%BD%92%18%C2%B8%8C0%A7u9.%CA_%922%C3%15%3BN%E4%F45%3DD%A6t%60E%5B%CA%02N%1E%5Drw%CC%7C%7D%CEU%107%F8%BC%B37%E7%8EW%C9i%9B%3C%F6%FD%CA%A0%E6Du%C4%A3%25%B7%DD%E1a8c%05f"
b="1%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%93%D0w%C9Ur%C1%89y+u%EB%A3c%28%D4Z%CF%E8%8E%F1%B9%5D%D4%FBy%7C%5D%8F%B2A%C6%02%AC%C0%09X%E6%5C%EC%E79b%824%E6ko%00%06%2C%1F%03%8F%AD%91%BD%92%18B%B8%8C0%A7u9.%CA_%922%C3%15%3BN%E4%F45%3DD%A6t%60%C5%5B%CA%02N%1E%5Drw%CC%7C%7D%CEU%107%F8%BC%B37%E7%8EW%C9i%9B%BC%F5%FD%CA%A0%E6Du%C4%A3%25%B7%DD%E1%E18c%05f"

print(MD5(a))
print(MD5(b))
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