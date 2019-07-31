"""
recursive: O(2^n) too slow
recursive with memonization is much better : O(nc)
dynamic programming also : O(nc)

weitght: 1 2 4 2 5
value:   5 3 5 3 2
total capacity: 
"""

w = [1,2,4,2,5] # weight
v = [5,3,5,3,2] # value
arr = [[None for _ in range(16)] for _ in range(6)]

def Knapsack(n, capacity):
    if arr[n][capacity] != None:
        return arr[n][capacity]
    if n == 0 or capacity == 0:
        result = 0
    elif w[n] > capacity:
        result = Knapsack(n-1, capacity)
    else:
        tmp1 = Knapsack(n-1, capacity)
        tmp2 = v[n] + Knapsack(n-1, capacity-w[n])
        result = max(tmp1, tmp2)
    arr[n][capacity] = result
    print("arr[{}][{}] = {}".format(n, capacity, result))
    return result

print(Knapsack(4, 10))
for i in range(len(arr)):
    print(arr[i])
