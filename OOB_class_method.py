class family(object):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	@staticmethod # take no argu
	def say_hello():
		print("hello...")
	@classmethod # take cls as argu
	def say_class_hello(cls):
		if cls.__name__ == "Son_Class":
			print("hello son")
		elif cls.__name__ == "Daughter_Class":
			print("hello daughter")

class Son_Class(family):
	def __init__(self, a, b, c):
		#family.__init__(self) # python 2
		super(Son_Class, self).__init__(a, b, c) # python 2 if there is variable
		# super().__init(a,b,c) # python 3 if there is variable
	def say_son_hello(self):
		print("say son hello")

class Daughter_Class(family):
	def __init__(self, a, b, c, d): # you can add additional argu in subclass constructor
		#family.__init__(self)
		super(Daughter_Class, self).__init__(a, b, c) # get var type from parent class
		self.d = d
	def say_daughter_hello(self):
		print("say daughter hello")

son = Son_Class(2,3,4)
son.say_hello()
son.say_class_hello()
son.say_son_hello()
daughter = Daughter_Class(1,2,3,4)
daughter.say_hello()
daughter.say_class_hello()
daughter.say_daughter_hello()
print(daughter.a)
print(daughter.b)
print(daughter.c)
print(daughter.d)