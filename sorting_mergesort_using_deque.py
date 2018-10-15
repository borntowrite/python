from collections import deque
    
def mergeSort(s):
    if len(s) == 0 or len(s) == 1:
        return s
    else:
        mid = int(len(s)/2)
        left = mergeSort(s[:mid])
        right = mergeSort(s[mid:])
        return merge(left,right)

def merge(a, b):
    c = []
    a = deque(a)
    b = deque(b)
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.popleft()
        else:
            c.append(b[0])
            b.popleft()
    # if len(a) == 0: # if len(a) is 1 and len(b) is 2, then add last b to c
    #     c += b
    # elif len(b) == 0:
    #     c += a
    if a:
        c += a
    elif b:
        c += b

    return c

s = [54,26,93,17,77,31,44,55,20]
print(mergeSort(s))
a = [1]
b = [2]
print(a+b)
