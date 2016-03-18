#import sys
#a = sys.argv[1]
a = raw_input()
b = len(a)
x = 0
for i in range(b):
	if a[i] == ")":
		x = x - 1
	elif a[i] == "(":
		x = x + 1

if x != 0 or a[0]==")":
	print "NotBalanced"
else:
	print "Balanced"