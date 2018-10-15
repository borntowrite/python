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
    
