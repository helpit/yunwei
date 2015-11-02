import csv
#导入CSV模块库
 
#1---读取文件
# reader(csvfile[,dialect="excel"][,fmtparam])
# csvfile :需要是支持迭代(Iterator)的对象，并且每次调用next方法的返回值是字符串(string)
#           通常的文件(file)对象，或者列表(list)对象都是适用的，如果是文件对象，打开是需要加"b"标志参数。
# dialect : 编码风格，默认为excel方式，也就是逗号(,)分隔  另外csv模块也支持excel-tab风格，也就是制表符(tab)分隔。
#           其它的方式需要自己定义，然后调用register_dialect方法注册，list_dialects方法来查询已注册的所有编码风格列表
# fmtparam :格式化参数，用来覆盖之前dialect对象指定的编码风格。
 
csvfile = file('csv_test.csv', 'rb')
reader = csv.reader(csvfile)        #读取文件
for line in reader:
    print line
csvfile.close()
 
#2---向文件中写入数据
# writer(csvfile[, dialect='excel'][, fmtparam])
# writerow          写一行
# writerows         写多行
 
#例子2-1
writer = csv.writer(file("1.csv","wb"))     #创建1.csv对象
writer.writerow(['c1', 'c2', 'c3'])
lines =[range(3) for i in range(5)]
for line in lines:
    writer.writerow(line)                   #按行写入
 
# 例子2-2
csvfile = file('csv_test.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['姓名', '年龄', '电话'])     #写入一行
data = [('张三', '25', '1234567'),('李四', '18', '789456')]
writer.writerows(data)                      #写入多行
csvfile.close()                             #关闭文件 
 
 
# DictReader
# 同reader差不多，都是读取CSV用的，只不过会生成一个字典(dict)类型的返回，而不是迭代类型
# DictWriter
rows = [{'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
        {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
        {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
        {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
        {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'}]
#这样就可以直接调用DictWriter.writerows方法来处理了:
 
fieldnames = ['Column1', 'Column2', 'Column3', 'Column4']
dict_writer = csv.DictWriter(file('your.csv', 'wb'), fieldnames=fieldnames)
dict_writer.writerow(fieldnames)    # CSV第一行需要自己加入
dict_writer.writerows(rows)         # rows就是表单提交的数据
 
# 解析文件
csvReader = csv.reader(open('avDecode_list.csv', 'rb'))    #以只读方式取得csv文件中内容 
for row in csvReader:                               #行循环 
    parameterStr = ','.join(row)                 #通过逗号连接每行每个单元格的内容     
    parameters = parameterStr.split(',')    #得到每个单元格的内容 
       
    name = parameters[1]          #将第一个单元格的内容赋值给name 
    component = parameters[2] 
    executiontype = parameters[3] 
    format = parameters[4] 
    inputFile = parameters[5] 
    mode = parameters[6]
