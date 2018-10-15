def function():
    print("ahhh")
    print("ahhhhhh 2")
print("this is outside the function")

b=[40, 30, 20, 10]
total=0
for e in b:
    total=total+e
print(total)

def function2(x):
    return 2*x

def function5(x):
    print(x)
    print("www")
                
name1="yk"
height_m1=2
weight_kg1=90

name2="yk's sister"
height_m2=1.8
weight_kg2=70

name3="yk's brother"
height_m3=2.5
weight_kg3=160

def bmi_calculator(name, height_m, weight_kg):
    bmi=weight_kg/(height_m**2)
    print("bmi: ")
    print(bmi)
    if bmi<25:
        return name + "not overweight"
    else:
        return name + "is overweight"

result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)

for i in range(1, 5):
    print(i)

a = 'youngjun'
b = 'lee'
print('first name : {}, last name: {}'.format(a, b))

#inner/outer function
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

my_func = outer_function("xxxxxxxx")
my_func()

#decorators
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Inside of decorator before calling the func")
        #return original_function(*args, **kwargs) # same behavior 
        original_function(*args, **kwargs)
    return wrapper_function

def callback(original_function):
    return original_function

##class decorator_class(object):
##    def __init__(self, original_function):
##        self.original_function = original_function
##    def __call__(self, *args, **kwargs):
##        print("call  method executed this before {}".format(self.original_function.__name__))
##        return self.original_function(*args, **kwargs)

@decorator_function
#@decorator_class
def display():
    print("display function ran")

@decorator_function
#@decorator_class
def display_info(name, age):
    print("display_info function ran with arg ({}, {})".format(name, age))

print("--------------------------------------------------------------")
decorated_display = decorator_function(display)
decorated_display()
print("--------------------------------------------------------------")
callback_func = callback(display)
callback_func()
print("--------------------------------------------------------------")
#if you use @decorator_function, then you can also call a function like below
display = decorator_function(display) 
display()
print("--------------------------------------------------------------")
display_info("john", 25)

















                
