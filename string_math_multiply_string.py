"""
# Time:  O(m * n)
# Space: O(m + n)
# Given two numbers represented as strings, return multiplication of the numbers as a string.
# Note: The numbers can be arbitrarily large and are non-negative.
"""
class Solution(object):
    def mulstring(self, string1, string2):
        total = 0
        for i in reversed(range(len(string1))):
            for j in reversed(range(len(string2))):
                x = int(int(string1[i])*pow(10,len(string1)-i-1)) 
                y = int(int(string2[j])*pow(10,len(string2)-j-1))
                total += x*y
                print("x = ", x, "y = ", y, "total = ", total)
        return total

string1 = "12"
string2 = "12"
print(Solution().mulstring(string1, string2))

