#################################################################
# Solution 1
#################################################################
"""
idea of this recursion is... 
p(a1, a2, a3, a4) = a1 + p(a2, a3, a4)
                  + a2 + p(a1, a3, a4)
                  + a3 + p(a1, a2, a4)
                  + a4 + p(a1, a2, a3)
p(a2, a3, a4)     = a2 + p(a3, a4)
                  + a3 + p(a2, a4)
                  + a4 + p(a2, a3)
do same for the rest... 
"""
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

data = list('123')
for p in permutation(data):
    print(p)

#################################################################
# Solution 2
#################################################################
def permu(num):
	result = []
	used = [False]*len(num)
	cur = []
	return permu_helper(num, result, cur, used)

def permu_helper(num, result, cur, used):
	if len(num) == len(cur):
		return result.append(cur[:])
	for i in range(len(num)):
		if not used[i]:
			used[i] = True
			cur.append(num[i])
			permu_helper(num, result, cur, used)
			cur.pop()
			used[i] = False
	return result

print(permu([1,2,3]))

#################################################################
# Solution 3
#################################################################
import itertools
for i in itertools.permutations('abc'):
   print(i)

