import sys, string

# Get the file name either from the commandline or the user
if len(sys.argv) < 2:
    name = raw_input("Enter the file name: ")
else:
    name = sys.argv[1]

inp = open(name,"r")

# initialise counters to zero; which also creates variables
words = 0  
lines = 0
chars = 0

for line in inp.readlines():
    lines = lines + 1
    
    # Break into a list of words and count them
    list = string.split(line)
    words = words + len(list)
    
    # count the characters in the line
    chars = chars + len(line)
    
print "%s has %d lines, %d words and %d characters" % (name, lines, words, chars)
inp.close()
