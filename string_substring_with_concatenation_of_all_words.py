words = ['foo', 'bar']
x = ''
s = 'barfoothefoobarman'
# need permutation of words... 
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = [] 
    for i in range(len(lst)):
        current = lst[i]
        before = lst[:i]
        after = lst[i+1:]
        for p in permutation(before + after):
            #print("l.append([{}] + {})".format(current, p))
            l.append([current] + p)
    return l

ret = permutation(list(words))

for words in ret:
	for word in words:
		x = x + word
	for i in range(len(s)-len(x)+1):
		if s[i:i+len(x)] == x:
			print("found!! - index :", i)
	x = ''