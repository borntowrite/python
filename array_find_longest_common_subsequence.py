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
            # print("-------------------- i = ", i)
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
                    # print("found - str1[{}]:{} == str2[{}]:{}".format(i, str1[i], j, str2[j]))
                    tmp.append(str1[i])
                    i += 1
                    break
                j += 1
            i += 1
        return tmp

print(Solution().find([1,5,2,6,3,7], [5,6,7,1,2,3]))

"""
CS Dojo
"""
class Solution2(object):

    def __init__(self):
        self.memo = [[None for _ in range(10)] for _ in range(10)]

    # recursive
    def LCS(self, P, Q, n, m):
        if n==0 or m==0:
            result = 0
        elif P[n-1] == Q[m-1]:
            result = 1 + self.LCS(P, Q, n-1, m-1)
        elif P[n-1] != Q[m-1]:
            tmp1 = self.LCS(P, Q, n-1, m)
            tmp2 = self.LCS(P, Q, n, m-1)
            result = max(tmp1, tmp2)
        return result

    # recursive with memonization
    def LCS_memonization(self, P, Q, n, m):
        if self.memo[n][m] != None:
            return self.memo[n][m]
        if n==0 or m==0:
            result = 0
        elif P[n-1] == Q[m-1]:
            result = 1 + self.LCS_memonization(P, Q, n-1, m-1)
        elif P[n-1] != Q[m-1]:
            tmp1 = self.LCS_memonization(P, Q, n-1, m)
            tmp2 = self.LCS_memonization(P, Q, n, m-1)
            result = max(tmp1, tmp2)
            self.memo[n][m] = result
        return result
    
    # bottom up dynamic programming 
    def LCS_bottomup(self, P, Q):
        for i in range(len(P)+1):
            for j in range(len(Q)+1):
                if i == 0 or j == 0:
                    self.memo[i][j] = 0
                elif P[i-1] == Q[j-1]:
                    self.memo[i][j] = self.memo[i-1][j-1]+1
                else:
                    self.memo[i][j] = max(self.memo[i-1][j], self.memo[i][j-1])
        return self.memo[len(P)][len(Q)]
                
print(Solution2().LCS([1,5,2,6,3,7], [5,6,7,1,2,3], 6, 6))
print(Solution2().LCS_memonization([1,5,2,6,3,7], [5,6,7,1,2,3], 6, 6))
print(Solution2().LCS_bottomup([1,5,2,6,3,7], [5,6,7,1,2,3]))
# print(LCS(['a', 'b'], ['b', 'c'], 2, 2))
# print(LCS(['a', 'b'], ['b', 'a'], 2, 2))
# print(LCS([1,5,2,6,3,7], [5,6,7,1,2,3], 6, 6))

