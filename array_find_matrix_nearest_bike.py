"""
map = [[0,   0,  0,  0,  0, "#"],
       [0,   0, "E", 0,  0, "#"],
       ["#","#","#","#", 0, "#"],
       [0,  "B", 0 , 0,  0,  0],
       [0,   0,  0,  0,  0, "B"]]
0 - freepath/road
# - building/wall
B - bike(goal)
E - employee(origin)

find nearest bike from E

use BFS
"""
import collections

class Solution(object):
    def findbike(self, arr, start):
        q = collections.deque([[start]])
        s = set([start])
        while q:
            path = q.popleft()
            y,x = path[-1]
            if arr[y][x] == "B":
                return path
            for y,x in ((y, x+1), (y, x-1), (y+1, x), (y-1, x)):
                if 0 <= y < len(arr) and 0 <= x < len(arr[0]) \
                and arr[y][x] != "#" and (y,x) not in s:
                    q.append(path + [(y,x)])
                    s.add((y,x))
        return path

campusmap = [[0,   0,  0,  0,  0, "#"],
            [0,   0, "E", 0,  0, "#"],
            ["#","#","#","#", 0, "#"],
            [0,  "B", 0 , 0,  0,  0],
            [0,   0,  0,  0,  0, "B"]]
print(Solution().findbike(campusmap, (1,2)))

