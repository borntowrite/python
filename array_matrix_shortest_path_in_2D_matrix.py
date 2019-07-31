import collections

def bfs(grid, start):
    Q = collections.deque([[start]])
    seen = set([start])
    while Q:
        path = Q.popleft()
        y, x = path[-1]
        if grid[y][x] == goal:
            return path
        for y2, x2 in ((y+1,x), (y-1,x), (y,x+1), (y,x-1)):
            if 0 <= x2 < width and 0 <= y2 < height and \
            grid[y2][x2] != wall and (y2, x2) not in seen:
                Q.append(path + [(y2, x2)])
                seen.add((y2, x2))

wall, clear, goal = "#", ".", "*"
width, height = 10, 5
grid = ["..........",
        "..*#...##.",
        "..##...#*.",
        ".....###..",
        "......*..."]
print(bfs(grid, (2, 5)))
