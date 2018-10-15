"""
Robot in a Grid w/ recursive
Direction : right and down
"""
#grid = [[0 for x in range(0,5)] for y in range(0,5)]
x_end = 4
y_end = 4
grid= [ [0,  0,   0,   0,     0],
        [0,  'x',  'x',  0,     0],
        [0,   0,    0,   0,     0],
        ['x', 'x',  0,   'x',    0],
        [0,   0,    0,   0,     0]]

memo=[]
def Grid(grid, y, x, memo):
    if [y,x] in memo:
        # print([y,x], " is already in ", memo)
        return
    if x <= x_end and y <= y_end:
        if grid[y][x] != 'x':
            # print("grid[{}][{}] = {}".format(y,x,grid[y][x]))
            memo.append([y,x])
            Grid(grid,y,x+1, memo)
            Grid(grid,y+1,x, memo)

    return memo

# print(grid)
print(Grid(grid,0,0, memo))



