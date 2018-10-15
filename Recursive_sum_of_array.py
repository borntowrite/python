
def sum(arr, n):
    if n <= 0:
        return 0
    print("sum(arr, {}) + {}".format(n-1, arr[n-1]))
    return sum(arr, n-1) + arr[n-1]

print(sum([1,2,3,4,5], 5))
