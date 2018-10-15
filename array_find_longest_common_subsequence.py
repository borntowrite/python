"""
Given two integer arrays. Find the longest common subsequence.
eg. 

input
str1 = [1,5,2,6,3,7] i
str2 = [5,6,7,1,2,3] j

output
return [1,2,3] or [5,6,7]
"""

class Solution(object):
    def find(self, str1, str2):
        result = []
        prev = 0
        for i in range(len(str1)):
            print("-------------------- i = ", i)
            ret = self.find_helper(str1, str2, i)
            if len(ret) >= prev:
                result.append(ret)
                prev = len(ret)
        return result
    
    def find_helper(self, str1, str2, str1_position):
        i, j = str1_position, 0
        tmp =[]
        while i < len(str1):
            while j < len(str2):
                if str2[j] == str1[i]:
                    print("found - str1[{}]:{} == str2[{}]:{}".format(i, str1[i], j, str2[j]))
                    tmp.append(str1[i])
                    i += 1
                    break
                j += 1
            i += 1
        return tmp

print(Solution().find([1,5,2,6,3,7], [5,6,7,1,2,3]))

