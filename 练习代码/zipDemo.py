#ta = [1,2,3]
#tb = [9,8,7]
#tc = ['a','b','c']
#for (a,b,c) in zip(ta,tb,tc):
#	print (a,b,c)

ta = [1,2,3]
tb = [9,8,7]
# cluster
zipped = zip(ta,tb)
print (zipped)

#decompose
na, nb = zip(*zipped)
print (na,nb)
