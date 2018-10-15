class graph:
	def __init__(self, gdict=None):
		if gdict is None:
			gdit = []
		self.gdict = gdict

	def getKeys(self):
		return list(self.gdict.keys())

	def getValues(self):
		return list(self.gdict.values())

	def findedges(self):
		edgename = []
		for key in self.gdict:
			for value in self.gdict[key]:
				if {key, value} not in edgename:
					edgename.append({key, value})
		return edgename

	def addNode(self, key):
		if key not in self.gdict:
			self.gdict[key] = []

graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)
print(g.getKeys())
print(g.getValues())
print(g.findedges())
g.addNode("f")
print(g.getKeys())