from __future__ import print_function
try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

"""
#
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
"""

# Math solution.
# Time:  O(n)
# Space: O(1)
class Solution(object):
    def numTrees(self, n):
        if n == 0:
            return 1
        def combination(n, k):
            count = 1
            # C(n, k) = (n) / 1 * (n - 1) / 2 ... * (n - k + 1) / k
            for i in xrange(1, k + 1):
                count = count * (n - i + 1) / i
            return count
        return combination(2 * n, n) - combination(2 * n, n - 1)

# DP solution.
# Time:  O(n^2)
# Space: O(n)
class Solution2:
    def numTrees(self, n):
        counts = [1, 1]
        for i in xrange(2, n + 1):
            count = 0
            for j in xrange(i):
                count += counts[j] * counts[i - j - 1]
            counts.append(count)
        return counts[-1]

# Time:  O(n)
# Space: O(1)
# Algo: Catalan Number
class Solution3(object):
    def numTrees(self, n):
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)

# Time:  O(n^2)
# Space: O(n)
# Algo: Catalan Number
# C0 = 1, C1 = 1, C2 = 2, C3 = 5, C4 = 14 .... 
class Solution4:
    def numTrees(self, n):
        G = [0]*(n+1)
        G[0] = 1
        G[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]

if __name__ == "__main__":
    print(Solution().numTrees(3))
    print(Solution2().numTrees(3))
    print(Solution3().numTrees(3))
    print(Solution4().numTrees(3))