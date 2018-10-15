###########################################
# Brute Force approach
# condition : array[i] = i
###########################################

arr = [-25, -10, 2, 3, 5, 6, 9, 10, 12, 23, 41, 143, 1234]
print(arr)
def findMagicIndex(n, arr):
    for i in range(n):
        if arr[i] == i:
            return i
    return -1

print("findMagicIndex",findMagicIndex(10, arr))

###########################################
# Recursive approach for binary search (very common)
# condition : array[mid] = mid
###########################################
        
def findMid(arr, start, end):
    if end < start:
        return -1
    mid = int((start+end)/2)
    if arr[mid] == mid:
        print("arr[mid]", arr[mid], "mid: ", mid)
        return mid
    elif arr[mid] > mid:
        print("find left", "arr[mid]", arr[mid], " < mid: ", mid)
        return findMid(arr, start, mid-1)
    elif arr[mid] < mid:
        print("find right", "arr[mid]", arr[mid], " > mid: ", mid)
        return findMid(arr, mid+1, end)

print("findMid", findMid(arr, 0, len(arr)-1))

###########################################
# if the elements are not distinct 
###########################################

arr2 = [-10, -5, 2,2,2,3,4,7,9,12,13]
# index   0     1  2 3 4 5 6 7  8  9  10
# arr2[7] = 7 
def findMid2(arr, start, end):
    if end < start:
        return -1
    mid = int((start+end)/2)
    midval = arr[mid]
    if midval == mid:
        print("midval",midval)
        return mid
    elif arr[mid] > mid:
        leftindex = min(mid-1, midval)
        return findMid2(arr, start, leftindex)
    elif arr[mid] < mid:
        rightindex = max(mid+1, midval)
        return findMid2(arr, rightindex, end)

print("return is" , findMid2(arr2, 0, len(arr)-1))

