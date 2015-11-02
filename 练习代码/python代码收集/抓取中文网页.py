import sys
import urllib.request
req = urllib.request.Request('http://www.baidu.com')
response = urllib.request.urlopen(req)
he_page = response.read()
type = sys.getfilesystemencoding() #转换成本地系统编码
  
print(the_page.decode(type))
