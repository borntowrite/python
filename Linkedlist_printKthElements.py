
############################################
# find K th linkedlist 
# single linkedlist
############################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.remove = False
    # kth element from tail
    def printKthElements(self, Node, k):
        if Node == None:
            return 0
        index =  self.printKthElements(Node.next, k) + 1
        if index == k:
            print("Found!! - {} th element: {}".format(k, Node.data))
        return index
    def printtree(self):
        while self != None:
            print(self.data)
            self = self.next
    def removeKthElements(self, Current, k):
        if Current == None:
            return 0
        index =  self.removeKthElements(Current.next, k) + 1
        if index == k:
            print("Remove!! - {} th element: {}".format(index, Current.data))
            self.remove = True
            return index
        if self.remove == True:
            Current.next = Current.next.next
            self.remove = False
        return index

Node1 = Node(3)
Node2 = Node(5)
Node3 = Node(6)
Node4 = Node(2)
Node5 = Node(412)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5

Node1.printKthElements(Node1, 1)
Node1.printtree()
Node1.removeKthElements(Node1, 1)
Node1.printtree()



