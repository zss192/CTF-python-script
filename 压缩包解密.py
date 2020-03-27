import zipfile
import os

name = 'hW1ES89jF'
tmp="" #解压过的文件
while True:
    fz = zipfile.ZipFile(name + '.tar.gz', 'r') #打开压缩包
    fz.extractall(pwd=bytes(name, 'utf-8')) #解密
    tmp=name+".tar.gz"
    os.remove(tmp)
    name = fz.filelist[0].filename[0:9] #获取压缩包里的文件名
    fz.close()