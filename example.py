import random
(n, m) = (10, 15)
(mx,s) = (
            [random.randint(0, 9) for _ in range(n*m)], 
            random.randint(1, 50)
        )
(v,l,r) = ([0]*m*n, [[[0], mx[0]]], [])
while l:
    nl = []
    for [p, ps] in l:
        if ps == s:
            r = p
            break
        if ps < s:
            pp = p[-1]
            for np in [pp + d for d in [-1, 1, -m, m]
                   if 0<=pp+d<n*m and abs((pp+d)%m - pp%m)<2 \
                   and v[pp+d] == 0]:
                v[np] = 1
                nl += [[p + [np], ps + mx[np]]]
    l = nl

def printm(mx):
    print("")
    for i in range(n):
        print('[' + ' '.join(map(str, mx[i*m:i*m+m])) + ']')
    
print("target =", s)
printm(mx)
if r:
    printm([1 if i in r else 0 for i in range(n*m)])