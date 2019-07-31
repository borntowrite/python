"""
Union Find = Disjoint Find 
Use-Case:
    1. Kruskal's minimum spanning
    2. tree algorithm
    3. grid percolation
    4. network connectivity
    5. least common ancestor in trees
    6. image processing
time Complexity: O(n)
"""

# example from geeks
from collections import defaultdict 
class Graph: 
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def find_parent(self, parent,i): 
        if parent[i] == -1: 
            return i 
        if parent[i] != -1: 
             return self.find_parent(parent,parent[i]) 

    def union(self,parent,x,y): 
        x_set = self.find_parent(parent, x) 
        y_set = self.find_parent(parent, y) 
        parent[x_set] = y_set 

    def isCyclic(self): 
        parent = [-1]*(self.V) 
        for i in self.graph: 
            for j in self.graph[i]: 
                x = self.find_parent(parent, i)  
                y = self.find_parent(parent, j) 
                if x == y: 
                    return True
                self.union(parent,x,y) 
    
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(1, 2) 
# g.addEdge(2, 0) 
g.addEdge(2, 3) 
  
if g.isCyclic(): 
    print("Graph contains cycle")
else : 
    print("Graph does not contain cycle ")
