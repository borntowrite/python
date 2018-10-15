import math
import statistics
from functools import reduce

############################
# map function 
############################
def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi*(r**2)

radii = [2,5,7.1, 0.3, 10]
areas = []
for r in radii:
    a = area(r)
    areas.append(a)
print(areas)

temps = [("Berlin", 29), ("Cario", 36)]
c_to_f = lambda data: (data[0], (9/5)*data[1]+32)
print(map(c_to_f, temps))
print(list(map(c_to_f, temps)))

############################
# filter function 
############################
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)
print(list(filter(lambda x: x > avg, data)))
print(list(filter(lambda x: x < avg, data)))

# remove missing data
countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "", "", "Venezuela"]
print(list(filter(None, countries)))
# "", 0, 0.0, 0j, [] list, () tuple, {} dictionary, False, None, instances which signal they're empty

############################
# reduce function 
############################
##Data: [a_1, a_2, a_3, ...., a_n]
##Function: f(x,y)
##
##reduce(f, data)
##    step 1: val_1 = f(a_1, a_2)
##    step 2: val_2 = f(val_1, a_3)
##    step 1: val_3 = f(val_2, a_4)
##    .
##    .
##    .
##    step n: val_n = f(val_n-1, a_n+1)
##    return van_n
##
##Alternatively:
##    return f(f(f(a_1, a_2), a_3), a_4), ...., a_n)

# Multiply all numbers in a list (reduce)
data = [2,3,5,76,7,8,3,4,6,10]
multiplier = lambda x, y: x*y
print(reduce(multiplier, data))
print(reduce(lambda x, y: x*y, data))

# Multiply all numbers in a list (for loop)
product = 1
for x in data:
    product = product * x
print(product)








