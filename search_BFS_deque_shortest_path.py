from collections import deque
"""
1 -> 2 -> 3
|    ^
4 -> 5 
"""

def maxDepth(root):
    if root == None: return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right)+1

def shortestpath(start, target):
    q = deque()
    q.append(start)
    DEPTH_OF_TREE = 6
    distance = [-1 for i in range(DEPTH_OF_TREE)] # init distance with -1 
    distance[start] = 0
    while q:
        parent = q.popleft()
        for n in parent.neighbors:
            if distance[n] == -1:
                distance[n] = distance[parent] + 1
                if n == target:
                    print("found!!")
                else:
                    q.append(n)
            else:
                # if distance[n] is updated, it means visited before hence skip
                pass

shortestpath(1, 2)







