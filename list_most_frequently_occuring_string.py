
def frequent(string):
    words = {}
    s = string.split()
    for word in s:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    print(sorted(words.items(), key=lambda x: x[1], reverse=True)[0])

s1 = "i am happy but do you happy"
frequent(s1)

# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', 
# '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
# '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
# 'pop', 'popitem', 'setdefault', 'update', 'values']


