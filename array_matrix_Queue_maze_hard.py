"""
you're given a 2D grid representing a maze. A 0 represents a path, a1 represents a wall, 
and a2 represents the goal. you can only move in the left, right, up or down direction.
return the list of coordinates that correspond to a valid solution(traveling along the path), 
given a starting location. if there are no valid path, return empty list.

Examples:
(3,0)

[[0,0,0,1],
 [0,0,2,1]
 [1,0,1,0]
 [0,0,0,0]]

=> [(3,0), (3,1), (2,1), (1,1), (1,2)]
"""

from queue import Queue

def solve_maze(start, maze):
        queue = Queue()
        queue.put((start, [])) 
        seen = set([start])
        while not queue.empty():
            ((i, j), path) = queue.get()
            new_path = path + [(i, j)]
            if maze[i][j] == 2:
                return new_path
            if is_valid_location((i-1, j), maze) and (i-1, j) not in seen:
                queue.put(((i-1, j), new_path))
                seen.add((i-1, j))
            if is_valid_location((i+1, j), maze) and (i+1, j) not in seen:
                queue.put(((i+1, j), new_path))
                seen.add((i+1, j))
            if is_valid_location((i, j-1), maze) and (i, j-1) not in seen:
                queue.put(((i, j-1), new_path))
                seen.add((i, j-1))
            if is_valid_location((i, j+1), maze) and (i, j+1) not in seen:
                queue.put(((i, j+1), new_path))
                seen.add((i, j+1))
        return []

def is_valid_location(location, maze):
        (i, j) = location
        return 0 <= i and i <len(maze) and 0 <=j and j < len(maze[0]) and maze[i][j] != 1

maze = [[0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0]]

maze2 = [[0, 1, 0], 
         [0, 0, 1],
         [0, 1, 2]]

print(solve_maze((3,0), maze))
print(solve_maze((1,0), maze2))
