"""
# Time:  O(n)
# Space: O(1)

# Compare two version numbers version1 and version1.
# If version1 > version2 return 1, if version1 < version2
# return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and
# contain only digits and the . character.
# The . character does not represent a decimal point and
# is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to
# version three", it is the fifth second-level revision of
# the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 13.37
"""

class Solution(object):
    def compare_version_num(self, ver1, ver2):
        length1 = len(ver1)
        length2 = len(ver2)
        i, j = 0, 0
        while i < length1 or j < length2:
            var1, var2 = 0, 0
            while i < length1 and ver1[i] != ".":
                var1 = var1*10 + int(ver1[i])
                i += 1
            while j < length2 and ver2[j] != ".":
                var2 = var2*10 + int(ver2[j])
                j += 1
            if var1 != var2:
                if var1 > var2:
                    return 1
                else:
                    return -1
            i += 1
            j += 1
        return 0

print(Solution().compare_version_num("1.12", "1.13")) # -1
print(Solution().compare_version_num("1.22", "1.13")) # 1
print(Solution().compare_version_num("1.10", "1.10")) # 0