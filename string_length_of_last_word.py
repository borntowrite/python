"""
# Time:  O(n)
# Space: O(1)
#
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a character sequence consists of non-space characters only.
# For example,
# Given s = "Hello World",
# return 5.
"""

class Solution(object):
    def lengthLastWord(self, string):
        i = 1
        while s[-i] != " ":
            i += 1
        return i-1

s = "Hello World"
print(Solution().lengthLastWord(s))

"""
# Time:  O(n)
# Space: O(n)
"""
class Solution2(object):
    def lengthLastWord(self, string):
        return len(string.strip().split(" ")[-1])

s = "Hello World"
print(Solution2().lengthLastWord(s))