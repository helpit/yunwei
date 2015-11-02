try:
	print "Starting a try block"
	for i in [1,2,3]:
		print i/0 # divide by zero!
	print "Ending a try block"
except:
	print "Caught an error"

try:
	print "First try"
	try:
		print "Second try"
		print "fred" ** 3 # TypeError
	except TypeError:
		print "Caught TypeError"
                raise
except TypeError:
	print "At the top level"
except:
	print "Caught something unexpected"