# Create the equivalent of: COPY MENU.TXT MENU.BAK

# First open the files to read(r) and write(w)
inp = open("menu.txt","r")
outp = open("menu.bak","w")

# read the file into a list then copy to
# new file
for line in inp.readlines():
    outp.write(line)

print "1 file copied..."

# Now close the files
inp.close()
outp.close()
