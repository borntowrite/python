
"""
a = [1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]
empty seat = 0
taken seat = 1
find seat most far away from taken seat

"""

def longestdistance(arr):
    max_cnt = float('-inf')
    tmp = []
    for i in range(len(arr)):
        if arr[i] != 1:
            left = i-1
            right = i+1
            current_cnt = 0
            while left > 0 and right < len(arr) and arr[left] != 1 and arr[right] != 1:
                left -= 1
                right += 1
                current_cnt += 1
            if current_cnt > max_cnt:
                max_cnt = current_cnt
                tmp.append(i)
    return tmp.pop() if tmp else False


print("position: ", longestdistance([1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]))
print("position: ", longestdistance([1]))
print("position: ", longestdistance([0]))
