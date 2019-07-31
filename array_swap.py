

import random
import bisect

# Space Complexity: O(1)
# Time Complexity: O(n)
def even_odd(a):
    even, odd = 0, len(a)-1
    while even < odd:
        if a[even] %2 == 0: # if a[even] is even
            even += 1
        else: # if a[even] is odd
            a[even], a[odd] = a[odd], a[even]
            odd -= 1
    return a

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]
    
if __name__ == "__main__":
    a = [1,2,3,4,5,6,7]
    a[0], a[len(a)-1] = a[len(a)-1], a[0]
    print (a)
    print(even_odd([2,1,4,5,6,7,11]))
    print(grade(60))

    b = [('red', 5), ('blue', 2), ('yellow', 3), ('white', 4)]
    b.sort(key=lambda x: x[0])
    print(b)
    b.insert(0,('black', 1))
    print(b)
    b.pop()
    print(b)
