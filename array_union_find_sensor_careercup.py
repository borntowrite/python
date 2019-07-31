# Assume all sensors are within a room, the actual width of the room does not matter.
def canGoFromLeftToRight(roomHeight, sensors, r):
    ids = list(range(len(sensors)))

    print(ids)
    def union(i,j):
        ids[find(i)] = find(j)

    def find(i):
        print("find: {} != {}".format(i, ids[i]))
        while (i != ids[i]):
            ids[i] = ids[ids[i]]
            i = ids[i]
        return i

    top = []
    bottom = []
    for i,[x,y] in enumerate(sensors):
        if y+r >= roomHeight: # overlaps top side of the room
            top += [i]
        if y <= r: # overlaps bottom side of the room
            bottom += [i]
    print("top:", top)
    print("bottom:",bottom)

    if not top or not bottom:
        return True

    # unite all sensors overlapping the top
    for i,j in zip(top, top[1:]):
        union(j,i)

    # unite all sensors overlapping the bottom
    for i,j in zip(bottom, bottom[1:]):
        union(j,i)
    print("Joined:",ids)
 
    # unite all sensors overlapping each other
    for i,[x,y] in enumerate(sensors):
        for I,[X,Y] in enumerate(sensors[i+1:],i+1):
            if (X-x)*(X-x) + (Y-y)*(Y-y) <= r*r:
                print("Final - union({},{})".format(i,I))
                union(I,i)

    
    a = find(top[0])
    b = find(bottom[0])
    print("Joined:",ids, a, b)
    return a != b

print(canGoFromLeftToRight(1, [(0,0), (0.1,0.2), (0.2, 0.3), (0.5,0.2),(0.7,0.4),(0.6,0.6),(0.7, 0.7), (0.8, 0.8), (1,1)], 0.5))
# print(canGoFromLeftToRight(1, [(0,0),(0.5,0.2),(0.7,0.4),(1,1)], 0.5))