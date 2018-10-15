def dup(s):
	temp = []
	for i in s:
		if i not in temp:
			temp.append(i)
	return temp

print(dup("abccaacbb"))
