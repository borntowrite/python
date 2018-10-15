

######################################
##Linear Search - O(n)
######################################
print("----------------------- Linear Search -----------------------")
arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
def index(x):
    for i in range(0,len(arr)):
        if arr[i] == x:
            print("Element is present at index :", i)
    return -1

index(110)

######################################
##Binary Search - O(n)
######################################
print("----------------------- Binary Search -----------------------")
def binarySearch (arr, l, r, x):
    if r >= l:
        mid = l + int((r - l)/2)
        if arr[mid] == x:
             return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1

arr2 = [ 2, 3, 4, 10, 40, 50 ]
x = 10
result = binarySearch(arr2, 0, len(arr2)-1, x)

if result != -1:
    print ("Element is present at index :",result)
else:
    print ("Element is not present in array")

