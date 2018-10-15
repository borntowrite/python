
#############################################################
#print keys having 2nd lowest value
#############################################################

marksheet= [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# this is same as above. Set() is not required here. 
#sh = sorted(list(set([b for a, b in marksheet])))[1]
sh0 = sorted(list([b for a, b in marksheet]))[0] 
sh1 = sorted(list([b for a, b in marksheet]))[1]
sh2 = sorted(list([b for a, b in marksheet]))[2]
sh3 = sorted(list([b for a, b in marksheet]))[3]
# sorted()[0,1,2,3,...etc] 0 returns 1st item in order and 1 returns next.. 
print(sh0)
print(sh1)
print(sh2)
print(sh3)
print('\n'.join([a for a, b in sorted(marksheet) if b == sh1]))

#############################################################
# Both sorting works 
#############################################################
li = [9,1,8,2,7,3,6,4,5]
s_li = sorted(li) # sort #1
print(s_li)
li.sort() # sort #2
print(li)

#############################################################
#testing list printout
#creating list 
#############################################################

nums = [1,2,3,4,5,6,7,8,9,10]
my_list1 = [n for n in nums]
print(my_list1)

my_list2 = [n*n for n in nums]
print(my_list2)

my_list3 = map(lambda n : n*n, nums)
print(my_list3)

a = set(["b", "a"])
a = list(a)
print(a)

ints = [1,2,3,4]
print(sorted(ints)[0])

##help(sorted)
##"""sorted(iterable, /, *, key=None, reverse=False)
##    Return a new list containing all items from the iterable in ascending order.
##    A custom key function can be supplied to customize the sort order, and the
##    reverse flag can be set to request the result in descending order."""
##
data = (5,6,1,23,43,6,7,1,4) # tuple
data1 = [2,35,1,2,5,65,1,2,3] # list
print(sorted(data))
print(sorted(data1))

string = "apppleasdfgasdf"
print(sorted(string))