__author__ = 'huagong'

def line_conf(a,b):
    def line(x):
        return ax + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))
