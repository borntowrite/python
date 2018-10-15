##########################################################
# self (pre) -> a -> b -> b.next
# self (pre) -> b -> a -> b.next 
#                    a(pre) -> a -> b -> b.next
#                    a(pre) -> b -> a -> b.next 
# ............
# T -> a -> b -> P
# P = b.next
# T -> b -> a -> P
##########################################################
class ListNode(object):
    def __init__(self, x):
            self.val = x
            self.next = None
    def __repr__(self):
            return "{} -> {}".format(self.val, self.next)

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            a, b, c = current.next, current.next.next, current.next.next.next
            current.next = b
            b.next = a
            a.next = c
            current = a
        return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
s = Solution()
print(s.swapPairs(head))
