# -*- coding: utf-8 -*-
#看到这里面python code这么少，就把以前的笔记再贴一个吧
 
#要生成两个日期间的所有日期
import datetime
 
d1=datetime .date( 2012,12 ,05) #开始日期
d2=datetime .date( 2012,12 ,12)  #结束日期
delta=d2 -d1         #日期的差值 delta.days是相差天数
for i in range (delta.days):
    date=d1.strftime('%Y-%m-%d')
    print date
    d1+=datetime.timedelta(days=1)     #datetime.timedelta(1)是把日期的差变为可以操作的格式
