from collections import Counter

#############################################################
#Counter ---> this will cound how many same element in list and come up with dictionary 
#############################################################
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print(Counter(myList))
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
print(Counter(myList).items())
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
print(Counter(myList).keys())
[1, 2, 3, 4, 5]
print(Counter(myList).values())
[3, 4, 4, 2, 1]

#############################################################
#Show Size - Hackerrank 
#############################################################
numSize = int(input())
print("number of shoe size: ", numSize)
# number of shoe size:  4
shoe = Counter(map(int, input().split()))
print(shoe)
# Counter({3: 2, 4: 2, 6: 2, 5: 1, 1: 1, 2: 1})
print("Size: {}, Price: {}".format(shoe.keys(), shoe.values()))
