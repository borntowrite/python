"""
definition of cyclic array is somewhat vague to me...

ex) 
p[1] = 5, p[5] = 1  ==> this is cyclic
p[1] = 1            ==> this is cyclic

"""
def cyclic(arr):
    n = len(arr)
    visited = set()
    
    for index in range(n):
        if index in visited:
            continue
        curr_visited = set()
        i = index
        while True:
            p = arr[i]
            if p < 0 or p >= n:
                break
            if p in curr_visited:
                return True
            if p in visited:
                print("here")
                break
            curr_visited.add(i)
            visited.add(i)
            i = p
    return False

print(cyclic([1,2,3,4,5,1]) == True)
print(cyclic([1,2,3,4,5,6]) == False)
print(cyclic([10,2,3,4,5,1]) == True)
print(cyclic([10,2,3,4,5,0]) == False)
print(cyclic([0,2,3,4,5,6]) == True)
print(cyclic([-8,-2,-3,-4,-5,4]) == False)
print(cyclic([-8,-2,-3,-4,5,4]) == True)
print(cyclic([1]))