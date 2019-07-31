
"""
You're given strings J representing the types of stones that are jewels,
and S representing the stones you have.  Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
"""

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        cnt=0
        for x in J:
            for y in S:
                if ord(x) == ord(y):
                    # print(ord(x), ord(y))
                    cnt += 1
        return cnt

if __name__ == "__main__":
    s = Solution()
    a = input("J=")
    b = input("S=")
    print(s.numJewelsInStones(a.strip('"'),b.strip('"')))
    # print(s.numJewelsInStones("aA","aAAbbb"))
    
