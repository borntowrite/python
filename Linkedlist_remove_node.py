from __future__ import print_function
# Time:  O(n)
# Space: O(1)
#
# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution(object):
	def removeNode(self, head, k):
		temp = ListNode(0) 
		temp.next = head # 0 1 2 3 4 5
		curr = temp.next # temp.next is 1 so move curr to 1 position
		prev = temp # 0 is prev node here, just in case we have to delete first node
		while curr:
			if curr.val == k:
				prev.next = curr.next 
			else:
				# otherwise, memory curr as prev node
				prev = curr
			# and move curr to next curr
			curr = curr.next 
		return temp.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(Solution().removeNode(head, 2))
