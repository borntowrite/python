
class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
	def insert(self, data):
		if self.data: 
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif self.data < data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data
	###################################################
	# Pre-Order Tree Traversal
	###################################################
	def preOrder(self, node):
		if node is not None:
			print(node.data) # mark node as visit
			self.preOrder(node.left)
			self.preOrder(node.right)
	###################################################
	# In-Order Tree Traversal
	###################################################
	def inOrder(self, node):
		if node is not None:
			self.preOrder(node.left)
			print(node.data) # mark node as visit
			self.preOrder(node.right)
	###################################################
	# Post-Order Tree Traversal
	###################################################
	def postOrder(self, node):
		if node is not None:
			self.preOrder(node.left)
			self.preOrder(node.right)
			print(node.data) # mark node as visit

d = Node(12)
d.insert(10)
d.insert(3)
d.insert(15)
d.insert(1)
d.insert(16)
print("preOrder")
d.preOrder(d)
print("inOrder")
d.inOrder(d)
print("postOrder")
d.postOrder(d)
