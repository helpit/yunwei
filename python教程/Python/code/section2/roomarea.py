totalLength = 14
lenA = 4.8
lenC = 4.1
widthA1 = 8
widthA2 = 5.2
widthC = 3.9

# calculate A and C areas first
A = lenA * widthA1
C = lenC * widthC

# calculate length and width of B
lenB = totalLength - (lenA + lenC)
widthB = widthA1 - widthA2

# now the area of B
B = lenB * widthB

# So the total area is:
Total = A + B + C
print "The total area is: ", Total
