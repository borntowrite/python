
import csv
path = "c:/work/python/movies.csv"

class movie:
	def __init__(self, path):
		self.path = path
		self.stack = {}
		self.capacity = 0
		self.minval = ""

	def setmovie(self, capacity):
		with open(self.path) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			header = next(csv_reader) # read out first line 
			for row in csv_reader:
				self.helper(row[0], int(row[1]), capacity)

	def helper(self, key, value, capacity):
		if key not in self.stack:
			self.stack[key] = value
		else:
			self.stack[key] += value
		if len(self.stack) > capacity:
			self.minval = min(self.stack.keys(), key=lambda k: self.stack[k])
			self.stack.pop(self.minval)

	def printmovie(self):
		print(self.stack)

m = movie(path)
m.setmovie(10)
m.printmovie()



        


            


