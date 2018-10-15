"""
de bruijn -> hard... 
"""

class Solution3(object):
    def crackSafe(self, n, k):
        # :type n: int
        # :type k: int
        # :rtype: str
        res = [0] * (n-1)   
        visited = set()
        if self.dfs(res, visited, n, k):
            return ''.join([str(m) for m in res])
        return ''

    def dfs(self, res, visited, n , k):
        if len(visited) == k ** n:
            return res
        for i in range(k):
            res.append(i)  
            new_key = tuple(res[len(res)-n:])
            print(new_key)
            if new_key not in visited:
                visited.add(new_key)
                if self.dfs(res, visited, n, k):
                    return True
                visited.remove(new_key)
            res.pop()
        return False        

print(Solution3().crackSafe(2, 3))

# try:
#     xrange
# except NameError:
#     xrange = range


# def de_bruijn_ize(st, k):
#     edges = []
#     nodes = set()
#     for i in range(len(st)-k+1):
#         edges.append((st[i:i+k-1], st[i+1:i+k])) # add as tuple 
#         nodes.add(st[i:i+k-1]) # set does not save dup item
#         nodes.add(st[i+1:i+k])
#     return nodes, edges

# nodes, edges = de_bruijn_ize('012345', 4)
# print(nodes)
# print(edges)

# nodes, edges = de_bruijn_ize('ACGCGTCG', 4)
# print(nodes)
# print(edges)

""" ==> you can use this on jupyter notebook to visualize 

def visualize_de_bruijn(st,k):
    nodes, edges = de_bruijn_ize(st, k)
    dot_str = 'digraph "DeBruijn graph" {\n'
    for node in nodes:
        dot_str += '  %s [label="%s"] ;\n' % (node, node)
    for src, dst in edges:
        dot_str += ' %s -> %s ;\n' % (src, dst)
    return dot_str + '}\n'

%load_ext gvmagic
%dotstr visualize_de_bruijn('ACGCGTCG', 3)
"""

""" Visualized Graph
 GC    AC
  \ ^\  /
    CG
   /  ^\
  GT   |
   \  / 
    TC 
"""

# class Solution(object):
#     def crackSafe(self, n, k):
#         seen = set()
#         ans = []
#         def dfs(node):
#             for x in map(str, range(k)):
#                 nei = node + x
#                 if nei not in seen:
#                     print(nei)
#                     seen.add(nei)
#                     dfs(nei[1:])
#                     ans.append(x)
#         dfs("0" * (n-1))
#         return "".join(ans) + "0" * (n-1)

# # crackSafe(n,k)
# # k = number list
# # n = length 
# print(Solution().crackSafe(6,2)) 

# class Solution2(object):
#     def crackSafe(self, n, k):
#         M = k**(n-1)
#         P = [q*k+i for i in xrange(k) for q in xrange(M)]
#         ans = []

#         for i in xrange(k**n):
#             j = i
#             while P[j] >= 0:
#                 ans.append(str(j / M))
#                 P[j], j = -1, P[j]

#         return "".join(ans) + "0" * (n-1)

# print(Solution2().crackSafe(3,3)) 
