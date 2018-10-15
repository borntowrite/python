"""
0 0 0 1 1 0 0
0 1 0 0 1 1 0
1 1 0 1 0 0 1
0 0 0 0 0 1 0 
1 1 0 0 0 0 0
0 0 0 1 0 0 0
"""
arr = [[0,0,0,1,1,0,0],
       [0,1,0,0,1,1,0],
       [1,1,0,1,0,0,1],
       [0,0,0,0,0,1,0],
       [1,1,0,0,0,0,0],
       [0,0,0,1,0,0,0]]

def findmaxarea(arr):
    maxsize, size = 0, 0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] == 1:
                size = getmaxsize(arr, row, col)
                maxsize = max(maxsize, size)
    return maxsize

def getmaxsize(arr, row, col):
    if row < 0 or col < 0 or row >= len(arr) or col >= len(arr[0]):
        return 0
    if arr[row][col]  == 0:
        return 0
    arr[row][col] = 0
    size = 1 # since self is 1 so begin size from 1 
    for i in range(row-1, row+2): # up and down
        for j in range(col-1, col+2): # left and right
            size += getmaxsize(arr, i, j)
    return size

print(findmaxarea(arr))
