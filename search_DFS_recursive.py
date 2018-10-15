# class graph:

#     def __init__(self,gdict=None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict
# Check for the visisted and unvisited nodes

# Original version in the web site
# def dfs(graph, start, visited = None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start)
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited

visited = []
def dfs(graph, start):
    if start in visited:
        return print("already visited")
    visited.append(start)
    print("visited: ", visited)
    for next in graph[start]:
        dfs(graph, next)
    return visited

gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e", "f"]),
                "e" : set(["a"]),
                "f" : set(["e", "d"])
                }

dfs(gdict, 'a')