
#########################################################
# iteration
#########################################################

def threesum1(x, w):
    temp = []
    for i in range(len(x)-2):
        for j in range(i+1, len(x)-1):
            for k in range(j+1, len(x)):
                if x[i]+x[j]+x[k] == w:
                    temp.append((x[i], x[j], x[k]))
    return temp

print("Solution-1: ",threesum1([-1, 0, 1, 2, -1, -4], 0))

#########################################################
# similar to permutation
#########################################################

def threesum2(nums, amount):
    temp=[]
    for i in range(len(nums)):
        current = nums[i]
        right = nums[i+1:]
        for c in helper(right):
            a = sorted([current]+c)
            if a not in temp and sum(a) == amount:
                temp.append(a)
    return temp

def helper(rest):
    temp = []
    for i in range(len(rest)-1):
        for j in range(i+1, len(rest)):
            # a = sorted([rest[i]]+[rest[j]]) # if there is dup num, better to use sort
            a = [rest[i], rest[j]]
            if not a in temp:
                temp.append(a)
    return temp

print("Solution-2: ",threesum2([-1, 0, 1, 2, -1, -4], 0))

#########################################################
# from geeksforgeeks, 
# brut-force
#########################################################
def findTriplets(arr, sum):
	temp = []
	n = len(arr)
	for i in range(0 , n - 2):
		for j in range(i + 1 , n - 1): 
			for k in range(j + 1, n):
				if (arr[i] + arr[j] + arr[k] == sum): 
					a = [arr[i],arr[j],arr[k]]
					if a not in temp:
						temp.append(a)
	return temp

print("Solution-3: ",findTriplets([-4,-1,-1,0,1,2], 0))
# print("Solution-3: ",findTriplets([1,2,3,4,5,6,7,8,9,10], 15))
# print("Solution-3: ",findTriplets([1,2,3,4,5,6,1,8,2,3], 15))

#########################################################
# using itertools
#########################################################
import itertools
nums = [-1, 0, 1, 2, -1, -4]
result = set()
for lst in itertools.combinations(nums, 3):
    if sum(lst) == 0:
        result.add(lst)
print("Solution-4: ", result)