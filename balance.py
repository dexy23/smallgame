#import sys
#a = sys.argv[1]
a = raw_input()
b = len(a)
x = 0
flag = True
for i in range(b):
	if a[i] == ")":
		x -= 1
	elif a[i] == "(":
		x += 1
	if x < 0:
	    flag = False

if flag and x == 0:
	print "Balanced"
else:
	print "NotBalanced"