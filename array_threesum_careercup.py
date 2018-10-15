"""
condition:
1. a[x]<a[y]<a[z]<a[w]
2. a[x]+a[y]+a[z]=a[w]

find all 3 sum that meets above condition 

"""


def find(nums):
    temp=[]
    for i in range(len(nums)):
        current = nums[i]
        right = nums[i+1:]
        for c in helper(right):
            a = sorted([current] + c)
            for amount in nums:
                if a not in temp and sum(a) == amount and a[0] < a[1] < a[2] < amount:
                    temp.append(a)
    print(temp)
    return len(temp)

def helper(a):
    temp = []
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if not [a[i], a[j]] in temp:
                temp.append([a[i], a[j]])
    return temp

""" all unique num, not sorted input, negative num included """ 
print("Solution-1: ",find([-1,0,1,2,3,-2,5]))
print("Solution-1: ",find([10,2,3,7,8,6,4,5,9,1]))

#######################################################################
# iteration 
#######################################################################

def find2(x):
    temp = []
    for i in range(len(x)-2):
        for j in range(i+1, len(x)-1):
            for k in range(j+1, len(x)):
                a = sorted([x[i], x[j], x[k]])
                for w in x:
                    if a[0]<a[1]<a[2]<w and a[0]+a[1]+a[2]==w:
                        temp.append((a[0], a[1], a[2]))
    print(temp)
    return len(temp)

print("Solution-2: ",find2([10,2,3,7,8,6,4,5,9,1]))