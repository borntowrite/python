import datetime

#############################################################
# printout format
#############################################################
class Person:
	"""docstring for Pname, ageon"""
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Person('Jack', '33')
sen = 'My name is {0.name} and I am {0.age} years old'.format(p1)
print(sen)

person = {'name':'jenn', 'age':23}
sen = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
print(sen)

sen = 'My name is {name} and I am {age} years old'.format(name='Jenn', age='33')
print(sen)

sen = 'My name is {name} and I am {age} years old'.format(**person)
print(sen)

pi = 3.14159265
sen = 'pi is equal to {}'.format(pi)
print(sen)
sen = 'pi is equal to {:.2f}'.format(pi)
print(sen)
sen = 'pi is equal to {:.3f}'.format(pi)
print(sen)

sen = '1MB is equal to {} bytes'.format(1000**2)
print(sen)
sen = '1MB is equal to {:,} bytes'.format(1000**2)
print(sen)
sen = '1MB is equal to {:,.2f} bytes'.format(1000**2)
print(sen)

mydate = datetime.datetime(2018, 5, 23)
print(mydate)

sen = '{:%B %d, %y}'.format(mydate)
print(sen)
