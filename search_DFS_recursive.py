class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.visited = []
        self.gdict = gdict

    # Original version in the web site
    def dfs1(self,graph, start, visited = None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start)
        for next in graph[start] - visited:
            self.dfs1(graph, next, visited)
        return visited
    
    def dfs2(self, graph, start):
        if start in self.visited:
            return print("already visited")
        print(start)
        self.visited.append(start)
        for next in graph[start]:
            self.dfs2(graph, next)
        return self.visited

gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e", "f"]),
                "e" : set(["a"]),
                "f" : set(["e", "d"])
                }

print(graph().dfs1(gdict, 'a'))
print(graph().dfs2(gdict, 'a'))