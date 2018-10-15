##############################################################
# Class Example 1
##############################################################
class Parent: 
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
	def print(self):
		print("I am Parent Class = ", self.first)
	class InnerChild:
		def __init__(self, name):
			self.name = name
			print("I am InnerChild->init = ", self.name)
		def print(self):
			print("I am InnerChild->print = ", self.name)

class Child(Parent):
	def __init__(self, first, last, pay, language):
		super().__init__(first, last, pay)
		#Parent.__init__(first, last, pay) # same as above
		self.language = language
	def print(self):
		super().print()

emp1 = Parent('fred', 'lee', 2000000)
print(emp1.InnerChild('baby'))
d = emp1.InnerChild('2nd baby')
d.print()
emp1.print()
emp2 = Child('claire', 'lee', 10000000000, 'python')
print(emp2.first)
print(emp2.language)
emp2.print()
a = emp2.InnerChild('3rd baby')
a.print()

##############################################################
# Class Example 2
##############################################################
class SimpleGradebook:
	def __init__(self):
		self._grades = {}
	def add_student(self, name):
		self._grades[name] = []
	def report_grade(self, name, grade):
		self._grades[name] = grade
	def average_grade(self, name):
		grades = self._grades[name]
		return grades

book = SimpleGradebook()
book.add_student('fred')
book.report_grade('fred', 100)
print(book.average_grade('fred'))

##############################################################
# Class Example 3
##############################################################
class Polynomial:
	def __init__(self, *coeffs):
		self.coeffs = coeffs
	def __repr__(self):
		return 'Polynomial(*{!r})'.format(self.coeffs)
	def __add__(self, other):
		return Polynomial(*(x+y for x,y in zip(self.coeffs, other.coeffs)))

p1 = Polynomial(1,2,3)
p2 = Polynomial(3,4,3)
print(p1+p2)

def multiarg(*x):
	for i in x:
		print("arguments :", i)

multiarg('a', 'b', 'c', 'd')

##############################################################
# Class Example 4
##############################################################

grades = []
grades.append((100, 1))
grades.append([100, 1])
grades.append({100, 1})
print(grades)
for a, b in grades:
	print(a, b)

