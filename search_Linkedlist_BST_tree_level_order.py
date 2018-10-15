# look at search_Linkedlist_BST_superset.py


from queue import Queue
########################################
# BST w/ linked list & recursion 
########################################
class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def insert(self, data): # recursive insersion 
        if self.data: 
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data < data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

########################################
# Tree Level Order 
########################################

    def traverse(self, node):
        if node == None: 
            return
        q = Queue()
        q.put(node)
        while not q.empty():
            curr = q.get()
            print("tree traverse:", curr.data) #print(toVisit.get().data) # this also works
            if curr.left: 
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)

"""
tree shape:
                12
             /      \ 
            10       15 
          /         /  \
         3        14    16
       /  
     1
"""
d = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))

# d = Node(12)
# d.insert(10)
# d.insert(3)
# d.insert(15)
# d.insert(1)
# d.insert(16)
# d.insert(14)
d.traverse(d)

            
            
        
