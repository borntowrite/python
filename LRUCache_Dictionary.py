#######################
# LRUCache w/ Dictionary
# Dos prompt command
# python -m cProfile LRUCache_Dictionary.py
#######################
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        # if lru cache capacity is full already
        if len(self.cache) >= self.capacity:
            # find least/oldest used
            # sort by lru[] value
            # return lru[] key
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            print("old_key :", old_key)
            self.cache.pop(old_key) # pop smallest value
            self.lru.pop(old_key) # pop smallest value
        self.cache[key] = value
        # whenever set which one is recently used
        # plus self.tm (count) to indicate which is latest
        self.lru[key] = self.tm  
        self.tm += 1
        # print("cache: ", self.cache)
        print("lru: ", self.lru)

    def printlru(self):
        print(self.lru)
    def printcache(self):
        print(self.cache)

cache = LRUCache(10)
cache.set('fred', 100)
cache.set('a', 200)
cache.set('b', 3300)
cache.set('c', 400)
cache.set('d', 500)
cache.set('d', 600)
cache.set('d', 700)
cache.set('a', 300)
cache.set('f', 234341)
cache.set('g', 234342)
cache.set('h', 234343)
cache.set('i', 2343445)
cache.set('j', 234346)
cache.set('k', 1346)
cache.set('l', 46)

print(cache.get('a'))
print(cache.get('f'))
print(cache.get('a'))
cache.printlru()
cache.printcache()


