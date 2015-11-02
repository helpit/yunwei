def spam(i,l=[]):
    l.append(i)
    return l

x = spam(10)
print x
y = spam(25)
print y
z = spam(50,[3])
print z

print x,y,z
