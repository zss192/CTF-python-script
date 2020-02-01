import base64
a = 'test'
e = base64.b64encode(b'test')    #e是加密，e是字节流
d= base64.b64decode(e)          #d是解密,d是字节流
print(e)
print(d)