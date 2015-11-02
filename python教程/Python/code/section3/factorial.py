def factorial(n):
    if (n < 0):
	 raise 'negative number error'
    if (n == 0) or (n == 1):
	 return 1
    else:
	 return n * factorial(n-1)

try:
    n = input('Try a number ')
    print factorial(n)
except 'negative number error':
    print 'cannot take factorial of a negative number'
except OverflowError:
    print 'number too long, try putting L at the end...'
