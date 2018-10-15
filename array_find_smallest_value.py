def smallest(arr):
    smallest = arr[0]
    for i in range(1, len(arr)-1):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

print(smallest([11,2,3,4,5,6,7,1,22,44,55]))