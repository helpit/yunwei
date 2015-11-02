#zip压缩文件操作
 
import zipfile
 
#1：zipfile.ZipFile(fileName[, mode[, compression[, allowZip64]]])
# r'表示打开一个存在的只读ZIP文件；
# 'w'表示清空并打开一个只写的ZIP文件，或创建一个只写的ZIP文件；
# 'a'表示打开一个ZIP
# compression表示压缩格式，压缩格式
# ZIP_STORE是默认的，表示不压缩；ZIP_DEFLATED表示压缩
# allowZip64为True时，表示支持64位的压缩
 
#2： zipfile.write(filename[, arcname[, compress_type]])
# acrname是压缩文件中该文件的名字，默认情况下和filename一样
# compress_type的存在是因为zip文件允许被压缩的文件可以有不同的压缩类型。
 
#3:　zipfile.extractall([path[, member[, password]]])
# path解压缩目录
# member需要解压缩的文件名儿列表
# password当zip文件有密码时需要该选项
 
f = zipfile.ZipFile('filename.zip', 'w' ,zipfile.ZIP_DEFLATED)  #创建ZipFile
f1 =zipfile.ZipFile('1.zip','a')        #创建空的压缩文件
 
f.write('file1.txt')
f.write('file2.txt')                #添加到压缩文件
f.close()                           #关闭文件，写入磁盘
 
f.extractall()                      #解压缩文件，默认当前目录
