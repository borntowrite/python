import collections
# class graph:
#     def __init__(self,gdict=None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict

def bfs(graph, startnode):
# Track the visited and unvisited nodes using queue
    seen, queue = set([startnode]), collections.deque([startnode])

    while queue:
        print("queue: {}, seen: {}".format(queue, seen))
        vertex = queue.popleft()
        print("pop from queue = {}, graph= {}]".format(vertex, graph[vertex]))
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

bfs(gdict, "a")