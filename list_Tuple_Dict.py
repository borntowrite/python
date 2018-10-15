#############################################################
# Tuple
#############################################################
nums = [1,1,2,1,3,4,3,4,5,6,7,8,7,8,9,10]
myset = set()
for n in nums:
   myset.add(n)
print(myset)
myset = {n for n in nums}
print(myset)

#############################################################
# Dict
#############################################################
##names = ['bruce', 'clark', 'peter', 'logan', 'wade']
##heros = ['batman', 'superman', 'spiderman', 'wolverine', 'deadpool']
##mydict = {}
##for name, hero in zip(names, heros):
##    mydict[name]=hero
##print(mydict)
##mydict = {name: hero for name, hero in zip(names, heros)}
##print(mydict)

#############################################################
# List
#############################################################
##nums = [1,2,3,4,5,6,7,8,9,10]
##mylist = [n for n in nums if n%2 ==0]
##print(mylist)

###Way-1
##mylist = []
##for letter in 'abcd':
##    for num in range(4):
##        mylist.append((letter,num))
##print(mylist)
###Way-2
##mylist = [(letter,num) for letter in 'abcd' for num in range(4)]
##print(mylist)
