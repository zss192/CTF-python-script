import zipfile
import os

name = '0653'
tmp="" #解压过的文件
while True:
    fz = zipfile.ZipFile(name + '.zip', 'r') #打开压缩包
    fz.extractall(pwd=bytes(name, 'utf-8')) #解密
    tmp=name+".zip"
    os.remove(tmp)
    name = fz.filelist[0].filename[0:4] #获取压缩包里的文件名
    fz.close()