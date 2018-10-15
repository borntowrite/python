########################################
# flip bit to win
########################################

def maxlen(n):
    if n & 255 == 255:
        return n.bit_length()
    currLen = 0
    prevLen = 0
    maxLen = 0
    while n != 0:
        if n & 1 == 1:
            currLen += 1
        elif n & 1 == 0:
            if n & 2 == 0: # & 10 -- if next bit is 0, means next bit is again 0
                prevLen = 0
            else: # % 10 -- if next bit is 1, means it can be connected with one bit flip
                prevLen = currLen
            currLen = 0
        maxLen = max(prevLen+currLen, maxLen)
        n = n >> 1
    return maxLen+1

print(maxlen(13))
print(maxlen(1775))
print(maxlen(15))
