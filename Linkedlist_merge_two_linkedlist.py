############################################
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# recursive
############################################
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    def __repr__(self):
        if self.next is None:
            return str(self.value)
        return str(self.value)+'->'+repr(self.next)

def merge(l1, l2):
    if l1 is None and l2 is None:
        return None
    elif l1 is None:
        return Node(l2.value, merge(l1, l2.next))
    elif l2 is None:
        return Node(l1.value, merge(l1.next, l2))
    elif l1.value < l2.value:
        return Node(l1.value, merge(l1.next, l2))
    else:
        return Node(l2.value, merge(l1, l2.next))

print(merge(None, None))
print(merge(None, Node(1)))
print(merge(Node(1, Node(2, Node(4))), Node(1, Node(3, Node(4)))))

############################################
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# iteration
############################################
class ListNode(object):
    """docstring for ClassName"""
    def __init__(self, val):
        self.val = val
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)
class Solution(object):
    def mergetwolinkedlist(self, p1, p2):
        head = curr = ListNode(0)
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        if p1 != None:
            curr.next = p1
        elif p2 != None:
            curr.next = p2
        return head.next
            
l1 = ListNode(0)
l1.next = ListNode(1)
l2 = ListNode (2)
l2.next = ListNode(3)
s = Solution()
print(s.mergetwolinkedlist(l1, l2))
