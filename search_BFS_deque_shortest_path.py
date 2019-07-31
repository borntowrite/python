from collections import deque
"""
a - b - d - e - a
|       | /
c       f
"""
class Solution(object):
    def shortestpath(self, graph, start, target):
        distance = [0 for x in range(1000)]
        q = deque()
        q.append(start)
        s = set(start)
        while q:
            parent = q.popleft()
            for n in graph[parent]:
                if n not in s:
                    distance[ord(n)] = distance[ord(parent)] + 1
                    q.append(n)
                    s.add(n)
        return distance[ord(target)]
"""
if graph is number, then it'll be much eaiser... 
then don't need set to remember visited node but instead
i can use distance as visited note at the same time i can also 
remember distance
"""
gdict = { "a" : set(["b","c"]),
        "b" : set(["a", "d"]),
        "c" : set(["a", "d"]),
        "d" : set(["e", "f"]),
        "e" : set(["a"]),
        "f" : set(["e", "d"])
        }

print(Solution().shortestpath(gdict, "a", "d"))
print(Solution().shortestpath(gdict, "a", "f"))






