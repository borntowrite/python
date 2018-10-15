from collections import defaultdict
from collections import namedtuple
from collections import OrderedDict
from collections import Counter
from collections import deque

#############################################################
# Find words & frequency from file and sort by key or value
#############################################################
d = OrderedDict()
with open('fred.txt', 'r') as f:
    for line in f:
        for word in line.split():
            if word not in d:
                d.update({word : 1})
                continue
            d[word] += 1
        
#for w in sorted(d, key=d.get, reverse=True): # sort by value, high->low
#for w in sorted(d, key=d.get, reverse=False): # sort by value, low->high
for w in OrderedDict(sorted(d.items(), key=lambda t: t[0], reverse = False)): 
#for w in OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse = True) ): 
    print(w, d[w])

def deleteDup(st, d):
    if st in d:
        d.pop(st)
    else:
        d.update({st:1})
    print(d)

deleteDup("amazon", d)
deleteDup("asfasdfa", d)

#help(d)
#print(d.items())
#print(d.values())
#print(d.keys())

















