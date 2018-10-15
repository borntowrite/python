"""
# Time:  O(n * 2^n)
# Space: O(2^n)
#
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.
"""

class Solution(object):
    def countsay(self, string):
        cnt, i, tmp = 1, 0, ""
        # a a b b c c c c c
        # 0 1 2 3 4 5 6 7 8
        while i < len(string):
            cnt = 1
            while i < len(string)-1 and string[i] == string[i+1]:
                cnt += 1
                i += 1
                # print(i, string[i], cnt)
            tmp += str(cnt) + string[i]
            i += 1
        return tmp

if __name__ == "__main__":
    print(Solution().countsay("aaabbccccc"))
    print(Solution().countsay("xxxyyyzzz"))