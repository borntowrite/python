
from collections import OrderedDict

#############################################################
# add values to orderedlist
# count frequency of each values
#############################################################
class Solution(object):
    def ordereddict(self, n, key):
        print("number of for-loop : ", n)
        d = OrderedDict()
        for i in range(n):
            if not key in d.keys():
                d.update({key : 1}) 
                continue
            d[key] += 1
            print(d)
        print(len(d.keys()))
        print(*d.values()) # print value only 
        print(d.values()) # print value like => odict_values([4, 1])

Solution().ordereddict(10, 2)