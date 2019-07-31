"""
1. normal dynamic programing
    time complexity: 
        call tree has n levels
        level 1 : 1 node
        level 2 : 2 node
        level 3 : 4 node
        level 4 : 8 node
        => 1*2*2*.. => O(2^n)
    space complexity: O(n) 

2. normal dynamic programing with memonization
    time complexity: O(n)
    space complexity: O(n) 
"""

# time complexity: O(2^n^2)
# space complexity: 
def countPaths(grid, row, col):
    if not validSquare(grid, row, col):
        return 0
    if isAtEnd(grid, row, col):
        return 1
    return countPaths(grid, row+1, col) + countPaths(grid, row, col+1)

# time complexity: O(n^2)
# space complexity: 
def countPaths_memonization(grid, row, col, paths):
    if not validSquare(grid, row, col):
        return 0
    if isAtEnd(grid, row, col):
        return 1
    if paths[row][col] == 0:
        paths[row][col] = countPaths(grid, row+1, col) + countPaths(grid, row, col+1)
    return paths[row][col]

def validSquare(grid, row, col):
    pass

def isAtEnd(grid, row, col):
    pass