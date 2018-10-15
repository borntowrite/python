#####################################################
# HackerRank - List 
#####################################################
# import random

# L=[]
# N = int(input())

# for row in range(N):
#     inputs = input().split()
#     if len(inputs)==1:
#         command =inputs[0]
#     if len(inputs)==2:
#         command = inputs[0]
#         e = int(inputs[1])
#     if len(inputs)==3:
#         command = inputs[0]
#         i = int(inputs[1])
#         e = int(inputs[2])

#     if command=="insert":
#         L.insert(i,e)
#     elif command=="remove":
#         L.remove(e)
#     elif command=="append":
#          L.append(e)
#     elif command=="sort":
#          L.sort()
#     elif command=="pop":
#          L.pop()
#     elif command=="reverse":
#          L.reverse()
#     elif command=="print":
#          print(L)

#####################################################
# HackerRank - List 
#####################################################
N = int(input())
lst = []
for i in range(0, N):
    inp = input().split(" ")
#    print("input value: ", inp)

    if inp[0] == "insert":
        lst.insert(int(inp[1]), int(inp[2]))
    if inp[0] == "print":
        print(lst)
    if inp[0] == "remove":
        lst.remove(int(inp[1]))
    if inp[0] == "append":
        lst.append(int(inp[1]))
    if inp[0] == "sort":
        lst.sort()
    if inp[0] == "pop":
        lst.pop()
    if inp[0] == "reverse":
        #lst.sort(reverse=True)
        lst.reverse()
