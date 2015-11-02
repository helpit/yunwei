# import os

inp = open("menu.txt","r")

for line in inp.readlines():
    print line[:-1]

inp.close()
