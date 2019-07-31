import time
from datetime import datetime

###################################################
# recursive - fibonacci
# time complexity : O(2^N)
###################################################
t_start = time.perf_counter()
def countways(x):
    if x < 0:
        return 0
    elif x == 0:
        return 1
    else:
        return countways(x-1) + countways(x-2)
print(countways(30))
t_end = time.perf_counter() 
print("Total Time = ", t_end-t_start)
###################################################
# recursive - memonization
# time complexity : O(N)
###################################################
# memo = {} # dict - hashmap
memo = [None]*100
t_start = time.perf_counter()
def fib_memo(x):
    if memo[x] is not None:
        return memo[x]
    if x == 0 or x == 1:
        result = 1
    else:
        result = fib_memo(x-1)+fib_memo(x-2)
    memo[x] = result
    return memo[x]
print(fib_memo(30))
t_end = time.perf_counter() 
print("Total Time = ", t_end-t_start)
###################################################
# Dynamic - bottomup
# time complexity : O(N)
###################################################
t_start = time.perf_counter()
def fib_bottomup(x):
    memo = [None]*(x+1)
    memo[0] = 1
    memo[1] = 1
    for i in range(2,x+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[x]    
print(fib_bottomup(30))
t_end = time.perf_counter() 
print("Total Time = ", t_end-t_start)


###################################################
# Another set of example
###################################################

def staircase(n):
    if n <= 1:
        return 1
    return staircase(n - 1) + staircase(n - 2)

# print(staircase(4))

def staircase2(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# print(staircase2(4))

def staircase3(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]

# print(staircase3(4, [1,2]))

###################################################
# Another set of example
###################################################
def num(n, arr):
    if n==0: return 1
    nums=[0 for i in range(0,n+1)]
    nums[0] = 1
    for i in range(1,n+1):
        total=0
        for j in arr:
            if i-j >=0:
                total += nums[i-j]
                # print("{} += nums[{}-{}]".format(total, i, j))
        nums[i] = total
        # print("nums[{}] = {}".format(i, nums[i]))
        # print("-----------------------------------------")
    return nums[n]
# arr=[1,3,5]
# print(num(6,arr))
arr1=[1,2,3]
#print(num(10,arr1))

