# f = open('test.txt')
# f.next()
# f.next()
# f.next()

for line in open('test.txt'):
	print line

def gen():
	a = 100
	yield a
	a = a*8
	yield a
	yield 1000

for i in gen():
	print i
	
def gen():
	for i in range(4):
		yield i

L = []
for x in range(10):
	L.append(x**2)
