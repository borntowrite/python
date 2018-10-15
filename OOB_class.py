
print("======================= Class Variable")
class test:
    def __init__(self):
        self.foo = 1
        self._bar = 2 
        self.__baz = 3 #can't access from outside of class

t = test()
print(t.foo)
print(t._bar)
#print(t.__baz) ---> #this doesn't work

t.foo = 3
print(t.foo)
t._bar = 4
print(t._bar)
print(t.__dict__)

print("======================= Class Override")

class Robot:
    def __init__(self, name, color, weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce(self):
        print("My name is " + self.name)
        print("My color is " + self.color)
        print("My weight is " + self.weight)

r1=Robot("fred", "blue", "42")
r2=Robot("mark", "red", "42")

r1.introduce()
r2.introduce()

class Person:
    def __init__(self, n, p, i):
        self.name=n
        self.personality=p
        self.is_sitting=i

    def sit_down(self):
        self.is_sitting=True

    def stand_up(self):
        self.is_sitting=False

p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

p1.robot_owned = r1
p2.robot_owned = r2
p1.robot_owned.introduce()

print("======================= Class Variables & Inheritance")

class Employee(object):
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1
    def apply_raise(self):
        #self.pay = int(self.pay  * raise_amount) --> error
        #self.pay = int(self.pay  * Employee.raise_amount) --> working
        self.pay = int(self.pay  * self.raise_amount) #--> working
    @property # decorator
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)
    @property # decorator
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None
    @classmethod # decorator
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    @classmethod # decorator
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    @staticmethod # decorator
    def is_workday(day): 
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    def __str__(self):
        return "{} - {}".format(self.fullname, self.email)
    def __len__(self):
        return len(self.fullname)
               
class Developer(Employee): # class inherited from Employee
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
                self.employees = []
        else:
                self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
                self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
                self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
                print('--->', emp.fullname)

dev_1 = Developer('Lewis', 'Lee', 1000, 'python')
dev_2 = Developer('Jake', 'Choi', 4000, 'java')

emp_1 = Employee("fred", "lee", 50000)
emp_2 = Employee("mark", "byun", 10000)
emp_3 = Employee("brandon", "lee", 40)

mgr_1 = Manager('yogi', 'chiniga', 100000, [dev_1])

print("---- built-in function ---")
print(len('test')) 
print('test'.__len__()) # same as above
print(len(emp_1)) # can use same string function here
print(emp_1.__len__()) # same as above

print(emp_1.__repr__()) 
print(repr(emp_1)) # same as above

print(emp_1.__str__())
print(emp_1) # same as above
print(str(emp_1)) # same as above

print("---- Decorator: Getter & Setter ---")
emp_1.fullname = 'Michael Jordan' # fullname.setter
print(emp_1.email) 
print(emp_1.fullname) 

del emp_1.fullname # fullname.deleter
print(emp_1.fullname)

#print(help(Developer))

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print(isinstance(mgr_1, Employee))
print(issubclass(Manager, Employee))

import datetime
my_date = datetime.date(2016, 7, 10)
print("---- Static Method ---")
print(Employee.is_workday(my_date))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print("---- Normal Method ----") 
print(emp_1.raise_amount)
print(Employee.raise_amount)
emp_1.raise_amount = 1.05
print(emp_1.__dict__)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print("---- Class Method ----") 
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = "john-doe-7000"
emp_str_2 = "steve-smith-3000"
emp_str_3 = "jane-doe-9000"

# common method
first, last, pay = emp_str_1.split("-")
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)

# use of class method
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)

print("=======================")




