#CRC32碰撞适用于压缩包内容较少且每个压缩包均含有相同字节数的情况
import zipfile
import string
import binascii

def CrackCrc(crc):
    for a in dic:
        for b in dic:
            for c in dic:
                for d in dic:
                    s = a + b + c + d   #每个data.txt内都有四个字节数据
                    if crc == (binascii.crc32(s) & 0xffffffff):  #通过不断拼接算出crc判断是否与已知crc相等
                        #print(s)
                        f.write(s)
                        return

def CrackZip():
    for i in range(68):
        file = 'out' + str(i) + '.zip'		#总共68个压缩包，分别为out0.zip out1.zip ....
        f = zipfile.ZipFile(file,'r')
        GetCrc = f.getinfo('data.txt')      #每个压缩包内都有一个名为data.txt的文件
        crc = GetCrc.CRC                    #以上几行为获取文件的CRC
        CrackCrc(crc)

dic = string.ascii_letters + string.digits + '+/='  #生成a-zA-Z0-9+/=

f = open('out.txt','w')
CrackZip()
f.close()
