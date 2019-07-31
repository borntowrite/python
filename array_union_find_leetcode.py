class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))

    def find_set(self, x):
        print("find_set : {} != {}".format(self.set[x], x))
        if self.set[x] != x:
            print("find_set : set[{}] = find_set({})".format(x,self.set[x]))
            self.set[x] = self.find_set(self.set[x]) 
        print("return {}".format(self.set[x]))
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        print("union_set: x_root = {}, y_root = {}".format(x_root,y_root))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        print("----------------------------------------------")
        return True 

class Solution(object):
    def findRedundantConnection(self, edges):
        union_find = UnionFind(len(edges)+1)
        for edge in edges:
            print("edge = {}".format(edge))
            if not union_find.union_set(*edge):
                return edge
        return []

print(Solution().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))

# map(function, list which is iteratable) which is same as :
# x_root = find_set(x), y_root = find_set(y)
