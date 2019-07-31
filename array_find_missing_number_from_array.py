"""
find missing num from given array (1~100)

Solution#1
1. compare two array (1~100 w/ missing num and 1~100)
2. minus and the diff is missing num

Solution#2
1. bitwise XOR(^) 
1 0 0 1
1 0 1 0
---------
0 0 1 1
2. ex) arr = [1,2,3,4,6,7,8]
    (1^2^3^4^6^7^8) ^ (1^2^3^4^5^6^7^8) = 5 
"""

class Solution1(object):
    def find_missing_number(self, arr, total):
        x1,x2 = arr[0],1
        for i in range(1, len(arr)):
            # print(i)
            x1 = x1 ^ arr[i]
        for j in range(2, 8+1):
            # print(j)
            x2 = x2 ^ j
        return (x1^x2)

print(Solution1().find_missing_number([1,2,3,4,6,7,8], 8))

class Solution2(object):
    def find_missing_number(self, arr, total):
        x1 = sum(arr)
        x2 = 1
        for i in range(2, 8+1):
            x2 = x2 + i
        return abs(x1-x2)

print(Solution1().find_missing_number([1,2,3,4,6,7,8], 8))