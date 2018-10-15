
###########################################################
# solution 1
###########################################################
class Solution(object):

    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.isPalindrome(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.isPalindrome(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def isPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

print(Solution().longestPalindrome("abcdcecd"))

###########################################################
# solution 2
###########################################################
def longestPalindrome(_str):
    if _str == None or len(_str) < 1: return ""
    start = 0
    end = 0
    for i in range(len(_str)):
        len1 = checker(_str, i, i)
        len2 = checker(_str, i, i+1)
        len3 = max(len1, len2)
        if len3 > end - start:
            start = i - int((len3-1)/2)
            end = i + int(len3/2)
    return _str[start:end+1]

def checker(_str, left, right):
    while left >= 0 and right < len(_str) and _str[left] == _str[right]:
        left -= 1
        right += 1
    return right - left - 1

print(longestPalindrome("abadcecd"))


