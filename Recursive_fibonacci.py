# @functools.lru_cache(maxsize=128, typed=False)
# Decorator to wrap a function with a memoizing callable that saves up 
# to the maxsize most recent calls. It can save time when an expensive 
# or I/O bound function is periodically called with the same arguments.
# Since a dictionary is used to cache results, the positional and keyword 
# arguments to the function must be hashable.
# If maxsize is set to None, the LRU feature is disabled and the cache 
# can grow without bound. The LRU feature performs best when maxsize 
# is a power-of-two.
# If typed is set to true, function arguments of different types will 
# be cached separately. For example, f(3) and f(3.0) will be treated 
# as distinct calls with distinct results.
# To help measure the effectiveness of the cache and tune the maxsize 
# parameter, the wrapped function is instrumented with a cache_info() 
# function that returns a named tuple showing hits, misses, maxsize 
# and currsize. In a multi-threaded environment, the hits and misses 
# are approximate.
# The decorator also provides a cache_clear() function for clearing 
# or invalidating the cache.
# The original underlying function is accessible through the __wrapped__ 
# attribute. This is useful for introspection, for bypassing the cache, 
# or for rewrapping the function with a different cache.
# An LRU (least recently used) cache works best when the most recent 
# calls are the best predictors of upcoming calls (for example, the most 
#     popular articles on a news server tend to change each day). 
# The cache’s size limit assures that the cache does not grow without 
# bound on long-running processes such as web servers.

import time
from datetime import datetime
from functools import lru_cache

#########################################################
# another example with fibonacci + lru_cache
#########################################################
@lru_cache(maxsize=None) # unlimited cache 
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(16)])
print(fib.cache_info())

#########################################################
# Improved fibonacci with LRU Cache - least recently used
# about lru_cache, see below 
#########################################################
print("fib - lru cache")
#t_start = datetime.now()
t_start = time.time()
@lru_cache(maxsize = 1000)
def fib1(n):
    # check that the input is a positive integer
    #if type(n) != int:
        #raise TypeError("n must be a positive int")
    if n < 1:
        #raise TypeError("n must be a positive int")
        return 0
    if n == 1:
        return 1
    elif n == 2: 
        return 1
    elif n > 2:
        return fib1(n-1) + fib1(n-2)

print([fib1(n) for n in range(500)])
#t_end = datetime.now()
t_end = time.time() 
print("Total Time = ", t_end-t_start)

#########################################################
# Improved fibonacci with Memonaization
#########################################################
print("fib - Memonaization")
t_start = time.time()
m = {}
def fib2(n):
    if n in m:
    #if memo[n] is not None:
        return m[n]
    if n == 0 or n == 1:
        value = 1
    elif n < 0:
        value = 0
    elif n == 2: 
        value = 1
    elif n > 2:
        value = fib2(n-1) + fib2(n-2)
    m[n] = value
    return value

for n in range(1,500):
    print(n, ":", fib2(n))
t_end = time.time() 
print("Total Time = ", t_end-t_start)

#########################################################
# Basic fibonacci 
#########################################################
print("fib - Normal")
t_start = time.time()
def fib3(n):
   if n == 0 or n == 1:
       return 1
   if n < 0:
       return 0
   elif n == 2: 
       return 1
   elif n > 2:
       return fib3(n-1) + fib3(n-2)

for n in range(1,10):
   print(fib3(n))

t_end = time.time() 
print("Total Time = ", t_end-t_start)

