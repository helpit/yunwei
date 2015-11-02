# try->异常->except->finally

# try->无异常->else->finally


re = iter(range(5))


try:
	for i in range(100):
		print re.next()
except StopIteration:
	print 'Here is end', i
	
print 'HaHaHaHa'
