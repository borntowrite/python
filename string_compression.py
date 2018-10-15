# e.g.
# compress('a') = a
# compress('aaa') = a3
# compress('aaabbb') = a3b3

def compress(s):
    sum = 1
    out = ""
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            sum += 1
        else:
            out = out + s[i] + str(sum)
            sum = 1
    out = out + s[len(s)-1] + str(sum)
    print(out)        

compress('aaabbbccc')