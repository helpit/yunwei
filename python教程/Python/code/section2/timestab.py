def print_table(multiplier):
    print "-------- Printing the %d times table ---------" % multiplier
    for n in range(1,13):
        print "%d x %d = %d" % (n, multiplier, n*multiplier)

if __name__ == "__main__":
	print_table(7)
