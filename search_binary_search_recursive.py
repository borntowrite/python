####################
# BST w/ array & half search
####################
arr_odd = [1,2,5,11, 22, 25, 33, 45, 77]
arr_even = [1,2,5,11, 22, 25, 33, 45, 77, 88]

def BSTSearch(arr, val, start, end):
    if start < end:
        mid = (start+end)//2
        if arr[mid] == val:
            print("found value = ", arr[mid])
        elif val < arr[mid]: # left search
            BSTSearch(arr, val, start, mid-1)
        elif arr[mid] < val: # right search
            BSTSearch(arr, val, mid+1, end)

BSTSearch(arr_odd, 5, 0, len(arr_odd)-1)
BSTSearch(arr_even, 77, 0, len(arr_even)-1)
