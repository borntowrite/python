"""
time complexity: O(n^2)
space complexity: O(1)

"""

class Solution(object):
    def bubblesort(self, arr):
        isSorted = False
        while not isSorted:
            isSorted = True
            for i in range(len(arr)-1):
                # print(i)
                if arr[i] > arr[i+1]:
                    self.swap(arr, i, i+1)
                    isSorted = False
        return arr
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        return arr

arr = [10, 2, 3, 8, 1]
print(Solution().bubblesort(arr))