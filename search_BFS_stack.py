#####################################
# BFS w/ stack
#####################################
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self, s):
        visited = [False] * (len(self.graph))
        stack = []
        stack.append(s)
        print("added to queue", s)
        visited[s] = True
 
        while stack:
            s = stack.pop()
            print ("popoed : ", s)
            print("self.graph[{}]={}".format(s, self.graph[s]))
            for i in self.graph[s]:
                print("visited[{}] = {}".format(i, visited[i]))
                if visited[i] == False:
                    print("added to queue", i)
                    stack.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(1, 0)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.BFS(0)
 

