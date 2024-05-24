import binascii

dic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+- ={}[]"
crc = 0x3DACAC6B  
for i in dic : 
    for j in dic:
        for p in dic:
            for q in dic:
                for a in dic:
                    s=i+j+p+q+a
                    if crc == (binascii.crc32(s) & 0xffffffff):
                        print s 
