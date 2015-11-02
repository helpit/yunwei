# 相当于(((1+2)+5)+7)+9

print reduce((lambda x,y: x+y), [1,2,5,7.9])
