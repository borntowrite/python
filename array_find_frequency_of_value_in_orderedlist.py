
from collections import OrderedDict

#############################################################
# add values to orderedlist
# count frequency of each values
#############################################################
n = int(input())
print("number of for-loop : ", n)
d = OrderedDict()

for i in range(n):
    key = input()
    if not key in d.keys():
        d.update({key : 1}) # d.update({key : value})
        # if input is new value, then add key : value first
        # next time since key is already there, won't come to here
        # but directly go to d[key] +=1
        continue
    d[key] += 1
    print(d)

print(len(d.keys()))
print(*d.values()) # print value only => 4 1
print(d.values()) # print => odict_values([4, 1])
