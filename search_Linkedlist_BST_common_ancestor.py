########################################
# solution to Low Common Ancesstor
# tree must be min heap already
########################################

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def commonAncesstor(self, root, a, b):
		pathToA = self.pathToX(root, a)
		pathToB = self.pathToX(root, b)

		result = None
		while pathToA and pathToB:
			popA = pathToA.pop()
			popB = pathToB.pop()
			if popA == popB:
				result = popA # or popB
				break
		return result	

	def pathToX(self, root, x):
		s = []
		if root is None:
			return None
		if root.value == x:
			print("Found path to {}".format(x))
			return s
		leftPath = self.pathToX(root.left, x)
		if leftPath is not None:
			leftPath.append(root.value)
			return leftPath
		rightPath = self.pathToX(root.right, x)
		if rightPath is not None:
			rightPath.append(root.value)
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
root = Node(12, Node(10, Node(3, Node(1), None), Node(11)), Node(15, None, Node(16)))
print('Common Ancestor is: ', root.commonAncesstor(root, 1, 16))