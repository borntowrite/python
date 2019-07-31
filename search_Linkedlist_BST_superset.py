from queue import Queue

""" Binary Search Tree """
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    """ Insert Node """
    def insert(self, data):
        if self.data: 
            if data < self.data:
                if self.left is None: self.left = Node(data)
                else: self.left.insert(data)
            elif self.data < data:
                if self.right is None: self.right = Node(data)
                else: self.right.insert(data)
        else:
            self.data = data

    """ Search Item """
    def search(self, data):
        if self.data == data: print("Found: ", self.data)
        elif data < self.data:
            if self.left is None: print("Data not found")
            else: return self.left.search(data)
        elif self.data < data:
            if self.right is None: print("Data not found")
            else: return self.right.search(data)

    """ Print All Trees """
    def printTree(self):
        if self.left: self.left.printTree()
        print(self.data)
        if self.right: self.right.printTree()

    """ Is Balanced """
    def isBalanced(self,node):
        if node is None:
            return True
        if abs(self.maxDepth(node.left) - self.maxDepth(node.right)) <= 1:
            return True
        return False

    """ max depth """ 
    def maxDepth(self,node):
        if node == None: return 0
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        return max(left, right)+1

    """ is binary search """
    def isBST(self, node):
        return self.isBST_helper(node, float('-inf'), float('inf'))
    
    def isBST_helper(self, node, min, max):
        if node is None:
            return True
        if node.data < min or node.data > max:
            return False
        return self.isBST_helper(node.left, min, node.data) and \
        self.isBST_helper(node.right, node.data, max)

    """ tree traversal """
    def traverse(self, node):
        if node == None: 
            return
        q = Queue()
        q.put(node)
        while not q.empty():
            curr = q.get()
            print("tree traverse:", curr.data) 
            #print(toVisit.get().data) # this also works
            if curr.left: 
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)

    """ pre order """
    def preOrder(self, node):
        if node is not None:
            print(node.data) # mark node as visit
            self.preOrder(node.left)
            self.preOrder(node.right)
            
    """ in order """
    def inOrder(self, node):
        if node is not None:
            self.preOrder(node.left)
            print(node.data) # mark node as visit
            self.preOrder(node.right)
    
    """ post order """
    def postOrder(self, node):
        if node is not None:
            self.preOrder(node.left)
            self.preOrder(node.right)
            print(node.data) # mark node as visit

    """ common parent node """
    def commonParentNode(self, root, a, b):
        pathToA = self.pathToX(root, a)
        pathToB = self.pathToX(root, b)
        while pathToA and pathToB:
            popA = pathToA.pop()
            popB = pathToB.pop()
            if popA == popB:
                return popA 
        return False

    def pathToX(self, root, x):
        s = []
        if root is None:
            return None
        if root.data == x:
            print("Found path to {}".format(x))
            return s
        leftPath = self.pathToX(root.left, x)
        if leftPath is not None:
            leftPath.append(root.data)
            return leftPath
        rightPath = self.pathToX(root.right, x)
        if rightPath is not None:
            rightPath.append(root.data)
            return rightPath
        return None

"""
tree shape:
                12
              /    \
            10      15
          /   \       \     
         3     11     16
        /
       1
"""
d = Node(12, Node(10, Node(3, Node(1), None), Node(11)), Node(15, None, Node(16)))

# d = Node(12)
# d.insert(10)
# d.insert(3)
# d.insert(15)
# d.insert(1)
# d.insert(16)
# d.insert(11)

d.printTree()
# d.search(3)
# d.search(300)

# if (d.isBalanced(d)): print("Balanced!!")
# else: print("Not Balanced!!")

# if (d.isBST(d)): print("It is BST")
# else: print("Not a BST")

# d.traverse(d)

# print("preOrder")
# d.preOrder(d)
# print("inOrder")
# d.inOrder(d)
# print("postOrder")
# d.postOrder(d)

# print("max depth :", d.maxDepth(d))

# print('Common Parent Node is: ', d.commonParentNode(d, 1, 16))
            
        
