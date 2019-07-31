import collections
class graph:
    # def __init__(self,gdict=None):
    #     if gdict is None:
    #         gdict = {}
    #     self.gdict = gdict

    def bfs(self, graph, startnode):
        seen = set([startnode])
        queue = collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            print(vertex)
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)

# The graph dictionary
gdict = { "a" : set(["b","c"]),
        "b" : set(["a", "d"]),
        "c" : set(["a", "d"]),
        "d" : set(["e", "f"]),
        "e" : set(["a"]),
        "f" : set(["e", "d"])
        }

graph().bfs(gdict, "a")