from __future__ import print_function

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution(object):
	def __init__(self):
		self.temp = ListNode(0)
		self.curr = self.temp

	# recursive - my own recursive solution. used global variable.
	def reverse(self, head):
		if not head:
			return None
		self.reverse(head.next)
		self.curr.next = ListNode(head.val)
		self.curr = self.curr.next
		return self.temp.next

	# iteration
	def reverse2(self, head):
		dummy = ListNode(float("-inf"))
		while head:
			dummy.next, head.next, head = head, dummy.next, head.next
			# if i do this, become infinite loop. don't know why!!! 
			# dummy.next = head
			# head.next = dummy.next
			# head = head.next
		return dummy.next

	def reverse3(self, head):
		curr = head
		prev = None
		"""
		prev addr:null
		addr:100, val:1, next:200
		next addr:200
		addr:200, val:2, next:300
		addr:300, val:3, next:400
		addr:400, val:4, next:500
		"""
		while curr:
			next_ = curr.next
			# next addr:200 = curr.next addr:200
			curr.next = prev
			# curr.next addr:null

			prev = curr
			# prev addr:100 = curr addr:100
			curr = next_
			# curr addr:200 = next addr:200
		head = prev
		return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(Solution().reverse(head))

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(Solution().reverse2(head))

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(Solution().reverse3(head))