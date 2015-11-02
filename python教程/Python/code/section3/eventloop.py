import msvcrt,sys

def doKeyEvent(key):
	print ord(key)

def doQuitEvent(key):
	sys.exit()
	
print """
Type a key to see its ASCII value.
Hit the space bar to end
"""

while 1:
    key = msvcrt.getch()
    if key <> ' ':
    	# handle special keys, real code is second
	if (key == '\000') or (key == '\xe0'):
		key = msvcrt.getch()
	# dispatch normal events
        doKeyEvent(key)
    else: # send the quit event 
    	doQuitEvent(key)

