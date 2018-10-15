from queue import Queue

s = set()
q = Queue()
start = (4,5)
end = [1]

q.put(((1,2), 3))
q.put(((4,5), 6))
q.put(((7,8), 9))
q.put(((10,11), 12))
while not q.empty():
    ((i, j), k) = q.get()
    print(i, j, k)

