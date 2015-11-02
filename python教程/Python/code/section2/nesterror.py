def nesterror():
    try:
        print 'Starting a try block'
        for i in [1,2,3]:
            print i/0 # divide by zero!
            print 'Ending a try block'
    except: # catches any error
        print 'Caught an error'

nesterror()
