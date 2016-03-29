lst = [1, 2, [3,4], 5, [[6, 7]]]
flag = False
while True:
	lst1 = []
	for elem in lst:
		if type(elem) != list:
			lst1.append(elem)
		else:
			for j in elem:
				lst1.append(j)
	lst = lst1
	flag = False
	for el in lst1:
		if type(el) == list:
			flag = True
	
	if flag == False:
		break
print lst1