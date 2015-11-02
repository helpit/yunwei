#! /usr/bin/env python
import sys,urllib
def reporthook(*a): print a   #reporthook函数会在每块数据下载或传输完成后被调用，
                                  #注释：用(block number, block size, total size)这三个参数调用reporthook函数。
for url in sys.argv[1:]:
       i = url.rfind('/')
       file = url[i+1:]
       print url,"-->",file
       urllib.urlretrieve(url,file,reporthook)   #返回二元组(filename, mime_hdrs)
