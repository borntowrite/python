#############################################################
# Lambda Sorting
#############################################################
from collections import OrderedDict
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
d = OrderedDict(sorted(d.items(), key=lambda t: t[0])) # sorting w/ key
for k, v in d.items():
   print(k, v)
d = OrderedDict(sorted(d.items(), key=lambda t: t[1])) # sorting w/ value
for k, v in d.items():
   print(k, v)

""" sort works but can't return sorted array or dict """
arr = {'fred': 3, 'claire':4, 'eunyoung': 1, 'house': 2}
# print(arr)
# print(sorted(arr.items(), key=lambda x: x[0]))
# print(sorted(arr.items(), key=lambda x: x[1]))
# print(arr.keys())
# print(arr.values())
