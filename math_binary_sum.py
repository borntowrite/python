"""
binary sum:

input: 
b' 0111
b' 0011

output: 1010
"""

class Solution(object):
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry = int(val / 2)
            val = int(val % 2)                                                                                                      
            # if 3, carry 3/2 = 1, val 3%2 = 1
            # if 2, carry 2/2 = 1, val 2%2 = 0
            # if 1, carry 1/2 = 0, val 1%2 = 1
            result += str(val) # add them but need to reverse later 
        if carry: # if there is leftover carry, then add them at the end
            result += str(carry)
        return result[::-1] # option -1 means "reverse the list"

print(Solution().addBinary('0111', '0011'))
