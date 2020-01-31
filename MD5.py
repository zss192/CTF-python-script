#MD5加密
import hashlib
def MD5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()

    
# print(MD5("abd"))


