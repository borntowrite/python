

######################################
##Linear Search - O(n)
######################################
print("----------------------- Linear Search -----------------------")
arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
def index(x):
    for i in range(0,len(arr)):
        if arr[i] == x:
            print("Element is present at index :", i)
    return -1

index(110)



