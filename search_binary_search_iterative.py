
###############################################
# iteration
###############################################
def binarysearch(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            high = mid - 1
        else: 
            low = mid + 1
    return False

print(binarysearch([1,2,3,4,5,6,7,8,9,10], 4))

