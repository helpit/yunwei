# 数字转各种进制, 输出字符
def toStr(n,base):
    converString = "0123456789ABCDEF"
    if n < base:
        return converString[n]
    return toStr(n//base, base) + converString[n%base]
