#!/usr/bin/env python
#coding:utf8
#Author:liaohg
#Email:liaohg@hojy.com
#Date:2015-03-23
#Function:Create the address book step by step
#
#Initialized variables
msg = '''
    1. Add information
    2. Display information
    3. Delete by name
    4. Update by name
    0. Exit 
'''
info = '''
    001. name
    002. gender
    003. tel
        004. all
'''
#txl content like this tex = [['name','gender','telphone'],['name','gender','telphone']]
txl = []
#define Add
def Add():
    name = raw_input('Please Enter Your name >>> ')
    gender = raw_input('Please Enter Your gender >>> ')
    tel = raw_input('Please Enter Your Telphone Number >>> ')
    txl.append([name,gender,tel])
#define display
def Disp():
    for list in txl:
        for info in list:
            print info,
            print ''
#define save
def Save():
    temp = []
    for info in txl:
        temp.append(','.join(info))
        s = '\n'.join(temp)
        fp = file('txl.db','w')
        fp.write(s+'\n')
        fp.close()
#define load
def Load():
    import os
    if  os.path.exists('txl.db'):
        fp = file('txl.db','r')
        content = fp.read()
        fp.close()
        temp = content.split('\n')
        for info in temp:
            txl.append(info.split(','))
    else:
        fp = file('txl.db','w')
        fp.close()
#define del
def Del():
    name = raw_input('Please Enter which one name you want to delete >>> ')
    for sub in txl:
        if sub[0] == name:
            txl.remove(sub)
            break
#define change 
def Change():
    xingming = raw_input('Please Enter which one name you want to change >>> ')
    print info
    op = raw_input('Please select which one you want to change: ')
    for sub in txl:
        if sub[0] == xingming:
            if op == '001':
                 name = raw_input('Please Enter Your name: ')
                 txl[txl.index(sub)][0] = name
            elif op == '002':
                 gender= raw_input('Please Enter Your gender: ')
                 txl[txl.index(sub)][1] = gender
            elif op == '003':
                 tel = raw_input('Please Enter Your tel: ')
                 txl[txl.index(sub)][2] = tel
        else:
         name = raw_input('Please Enter Your name: ')
         gender= raw_input('Please Enter Your gender: ')
         tel = raw_input('Please Enter Your tel: ')
         txl[txl.index(sub)] = [name,gender,tel]    
         break
Load()
while True:
    print msg
    op = raw_input('Please Select >>> ')
    if op == '1':
        Add()
        Save()
    elif op == '2':
        Disp()
    elif op == '3':
        Del()
        Save()
    elif op == '4':
        Change()
        Save()
    elif op == '0':
        break
    else:
        print ''
        print 'Unkonw Choose,Please Select again!'
        print ''
