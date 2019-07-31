###############################################
# in the interview, 
# better to use helper func for recursive always
###############################################

def halfSearch(arr, target):
    left = 0
    right = len(arr)-1
    return halfSearch_helper(arr, target, left, right)
    
def halfSearch_helper(arr, target, left, right):
    if left < right:
        mid = (left+right)//2
        if arr[mid] == target:
            print("found!!", arr[mid])
            return True
        elif arr[mid] < target: 
            halfSearch_helper(arr, target, mid+1, right)
        elif target < arr[mid]:
            halfSearch_helper(arr, target, left, mid-1)
    
print(halfSearch([1,2,5,6,7,8,9,11,25,263,277], 5))

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