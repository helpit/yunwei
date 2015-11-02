import sys

for arg in sys.argv:
    print 'arg = ', arg

if len(sys.argv) > 1:
    print '1st real arg is:', sys.argv[1]
    
    
