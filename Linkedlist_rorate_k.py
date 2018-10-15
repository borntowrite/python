from __future__ import print_function
# Time:  O(n)
# Space: O(1)
#
# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution(object):
 
    def rotateRight(self, l1, l2, k):

        n = 1
        curr = l1
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = l1 # 1 2 3 4 curr(5) + 1 2 3 4 5 + 1 2 3 4 5 ... infinite loop
        curr = l1 # curr(1) 2 3 4 5 1 2 3 4 5 ... move curr to 1
        # for _ in range(10):
        #     print(curr.val)
        #     curr = curr.next
        # tail = curr # wihtout this, works fine
        for _ in range(n - k):
            tail = curr # add 1 2 3 
            curr = curr.next # when exit for loop, curr is 4
        tail.next = None # 1 2 3 None
        return curr # curr is 4 so 4 5 1 2 3 None

    def rotateRight2(self, root, k):
        n = 1
        node = root

        # make infinite loop 
        while node.next:
            node = node.next
            n += 1
        node.next = root

        for _ in range(n-k):
            root = root.next
        node = root

        for _ in range(n-1):
            node = node.next
        node.next = None

        return root


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head2 = ListNode(6)
head2.next = ListNode(7)
head2.next.next = ListNode(8)
head2.next.next.next = ListNode(9)
head2.next.next.next.next = ListNode(10)
print(Solution().rotateRight(head, head2, 2))
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(Solution().rotateRight2(head, 2))