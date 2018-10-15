"""
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
"""

class ListNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None
	def __repr__(self):
		return "{}->{}".format(self.val, self.next)

class Solution(object):
	def twosum(self, a, b):
		num1, num2, carry = a, b, 0
		temp = ListNode(0)
		curr = temp
		while num1 and num2 :
			total = num1.val + num2.val + carry
			remaining = total%10
			carry = int(total/10)
			curr.next = ListNode(remaining)
			curr = curr.next 
			if num1: 
				num1 = num1.next
			if num2: 
				num2 = num2.next
		if carry == 1:
			curr.next = ListNode(carry)
		return temp.next

head1 = ListNode(2)
head1.next = ListNode(4)
head1.next.next = ListNode(3)
print(head1)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)
print(head2)

print(Solution().twosum(head1, head2))









