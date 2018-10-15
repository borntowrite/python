"""
1 2 3 4 5 
->
1 3 5 2 4
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution(object):
    def oddeven(self, head):
        if head:
            oddtail = head
            curr = head.next 
            while curr and curr.next:
                print("curr = ", curr.val)
                print("evenhead = oddtail.next", oddtail.next)	
                evenhead = oddtail.next
                print("oddtail.next = curr.next", curr.next)
                oddtail.next = curr.next 
                print("oddtail = oddtail.next", oddtail.next)             
                oddtail = oddtail.next 
                print("curr.next = oddtail.next", oddtail.next)
                curr.next = oddtail.next 
                print("oddtail.next = evenhead", evenhead)
                oddtail.next = evenhead
                curr = curr.next
                print(head)
                print("---------------------------------------")
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(Solution().oddeven(head))
