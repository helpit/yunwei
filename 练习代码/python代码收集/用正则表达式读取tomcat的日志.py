import re
regx = "\d\d\d\d-\d\d-\d+"
f = open("c:\stdout.log","r")
i = 0
for str in f.readlines():
   if re.search(regx,str):
        Response.write(str+"<br>")
         if i>10:break#由于是测试，只分析十行
         i=i+1
f.close();
