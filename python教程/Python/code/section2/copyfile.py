# Create the equivalent of: COPY MENU.TXT MENU.BAK
# First open the files to read(r) and write(w)
inp = open("C:\\autoexec.bat","r")
# outp = open("menu.bak","w")

# read file line by line until eof (line becomes false)
# copy each line to ouput file
line = inp.readline()
while line:
	print line
	line = inp.readline()
print "1 file copied..."

# Now close the files
inp.close()
# outp.close()
