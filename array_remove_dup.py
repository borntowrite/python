# return new length of array

def removeDup(arr):
    if len(arr) == 0:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i+1

print(removeDup([1,2,3,3,3,3,4,5]))

# Given an array nums and a value val, remove all 
# instances of that value in-place and return the new length.

def removeElement(arr, val):
    if len(arr) == 0:
        return 0
    i = 0
    for j in range(0, len(arr)):
        if arr[j] != val:
            arr[i] = arr[j]
            i += 1
    return i

print(removeElement([1,2,3,4,5], 3))