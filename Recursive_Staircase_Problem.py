###################################################
# recursive - dynamically
###################################################
def num(n, arr):
    if n==0: return 1
    nums=[0 for i in range(0,n+1)]
    nums[0] = 1
    for i in range(1,n+1):
        total=0
        for j in arr:
            if i-j >=0:
                total = total + nums[i-j]
                print("{} = total + nums[{}-{}]".format(total, i, j))
        nums[i] = total
        print("nums[{}] = {}".format(i, nums[i]))
        print("-----------------------------------------")
    return nums[n]
# arr=[1,3,5]
# print(num(6,arr))
arr1=[1,2,3]
print(num(10,arr1))

""" OUTPUT:
1 = total + nums[1-1]
nums[1] = 1
-----------------------------------------
1 = total + nums[2-1]
2 = total + nums[2-2]
nums[2] = 2
-----------------------------------------
2 = total + nums[3-1]
3 = total + nums[3-2]
4 = total + nums[3-3]
nums[3] = 4
-----------------------------------------
4 = total + nums[4-1]
6 = total + nums[4-2]
7 = total + nums[4-3]
nums[4] = 7
-----------------------------------------
7 = total + nums[5-1]
11 = total + nums[5-2]
13 = total + nums[5-3]
nums[5] = 13
-----------------------------------------
13 = total + nums[6-1]
20 = total + nums[6-2]
24 = total + nums[6-3]
nums[6] = 24
-----------------------------------------
24 = total + nums[7-1]
37 = total + nums[7-2]
44 = total + nums[7-3]
nums[7] = 44
-----------------------------------------
44 = total + nums[8-1]
68 = total + nums[8-2]
81 = total + nums[8-3]
nums[8] = 81
-----------------------------------------
81 = total + nums[9-1]
125 = total + nums[9-2]
149 = total + nums[9-3]
nums[9] = 149
-----------------------------------------
149 = total + nums[10-1]
230 = total + nums[10-2]
274 = total + nums[10-3]
nums[10] = 274
-----------------------------------------

"""

###################################################
# recursive - normal
# staircase - 1,2,3 step
# runtime : 3^n
###################################################

def countways(x):
    if x < 0:
        return 0
    elif x == 0:
        return 1
    else:
        return countways(x-1) + countways(x-2) + countways(x-3)

print(countways(10))

###################################################
# recursive - memonization
###################################################
memo = {} # dict - hashmap 
def countways_memo(x):
    if x < 0:
        return 0
    elif x == 0:
        return 1
    else:
        memo[x] = countways(x-1) + countways(x-2) + countways(x-3)
    return memo[x]

print(countways_memo(10))