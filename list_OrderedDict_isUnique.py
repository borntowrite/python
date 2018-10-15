###############################################
# is unique character? no dup? 
# with OrderedDict
###############################################
from collections import OrderedDict

d = OrderedDict()

def isUnique(string):
   if len(string) >128:
       return False
   for char in string:
       if char in d:
           return False
       d.update({char : True})
   print(d)
   return True

x=isUnique("melonggg")
print(x)
y=isUnique("melong")
print(y)