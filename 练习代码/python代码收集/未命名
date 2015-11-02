# -*- coding: cp936 -*-
import os
import hashlib
 
 
def file2md5(filename):
    fp = open(filename)
    data = fp.read()
    digest = hashlib.md5(data).digest()
    fp.close()
    return digest
 
 
# 返回指定目录下所有的文件名的迭代器，不递归目录
def filenames(dir_name):
    return ('%s/%s' % (dir_name, item) for item in os.listdir(dir_name) if os.path.isfile('%s/%s' % (dir_name, item)))
 
 
# 返回指定目录下所有文件名的迭代器，递归子目录
def xxx(dir_name):
    for item in os.listdir(dir_name):
        path = '%s/%s' % (dir_name, item)
        if os.path.isfile(path):
            yield path
        elif os.path.isdir(path):
            for x in xxx(path):
                yield x
 
 
items = xxx('.')
# 对每一个文件计算MD5
items = [(file2md5(item), item) for item in items]
# 删除重复文件
items.sort()
last = ''
for item in items:
    if last == item[0]:
        print 'remove file:', item[1]
        os.remove(item[1])
    else:
        last = item[0]
