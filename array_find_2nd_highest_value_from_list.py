#############################################################
#Printout 2nd highest value from list - Hackerrank
#############################################################
n = int(input())
arr = map(int, input().split())
arr = [2,3,6,6,5]
arr=sorted(arr)
print(arr)
maxnum = max(arr)
while max(arr) == maxnum:
    arr.pop()
    print(arr)

print(max(arr))
