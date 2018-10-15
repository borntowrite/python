"""
given an integer array, find out the equal sum partition with the smallest sum.
for example)
a = [1,3,2,2,1,3]
there are three equal sum partitions:
    1. [(1,3), (2,2), (1,3)]
    2. [(1,3,2), (2,1,3)]
    3. [(1,3,2,2,1,3)]
first one has smallest equal sum, so return 4

"""

def findsub(a):
    minsum = float('inf')
    if len(a) == 0:
        return False
    if len(a) == 1:
        return a[0]
    for i in range(2, len(a)+1):
        if len(a) % i == 0:
            minsum = min(minsum, isSumSame(a, i))
    return minsum

def isSumSame(a, i):
    subsum = 0
    prev = 0
    for x in range(0, len(a), i):
        subsum = 0
        for y in range(x, x+i):
            subsum += a[y]
        if prev > 0:
            if prev != subsum: # next sume is different from previous one
                return False
        prev = subsum
    return subsum

print("min sub sum is ", findsub([1,3,3,4,1,3,3,4]))
print("min sub sum is ", findsub([1,3,2,2,1,3]))
print("min sub sum is ", findsub([1,-1,2,-2,2,-2]))
print("min sub sum is ", findsub([1,3,1,3]))
print("min sub sum is ", findsub([1,3]))
print("min sub sum is ", findsub([1]))
print("min sub sum is ", findsub([1,2,3]))
print("min sub sum is ", findsub([]))
print("min sub sum is ", findsub([1,3,1,4,1,3]))        
    

