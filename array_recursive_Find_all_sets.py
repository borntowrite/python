###########################################
# Write a method to return all subsets of a set
# ex) [1,2] = [], [1], [2], [1,2] --- total 4 sets
###########################################

def sub_easylook1(arr):
        temp = []
        if arr == []:
                temp.append([])
                return temp
        ret = sub_easylook1(arr[1:])
        # print("ret=", ret, "arr=", arr)
        for n in ret:
                temp.append([arr[0]] + n)
        return ret + temp

ret = sub_easylook1([1,2,3])
print(ret)
for i in ret:
        if sum(i) == 4:
                print(i)
"""
def subs(arr):
        if arr == []:
                return [[]]
        x = subs(arr[1:])
        return x + [[arr[0]] + y for y in x]

print (subs([1, 2, 3]))
"""
     

















