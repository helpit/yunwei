import re
# detect 'IMG' or 'img' allowing for
# zero or more spaces between the < and the 'I'
img = '< *[Ii][Mm][Gg] ' 	
# allow any character up to the 'ALT' or 'alt' before >
alt = img + '.*[Aa][Ll][Tt].*>'

# open file and read it into list
filename = raw_input('Enter a filename to search ')
inf = open(filename,'r')
lines = inf.readlines()

# if the line has an IMG tag and no ALT inside
# substitute our message as an HTML comment
for i in range(len(lines)):
	if re.search(img,lines[i]) and not \
		re.search(alt,lines[i]):
		lines[i] = '<!-- PROVIDE ALT TAGS ON IMAGES! -->\n' \
			   + lines[i]

# Now write the altered file and tidy up.
inf.close()
outf = open(filename,'w')
outf.writelines(lines)
outf.close()
