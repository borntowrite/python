######################################################
# solution 1
######################################################

from __future__ import print_function
# Time:  O(nlogk)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):		
        if self:		
            return "{} -> {}".format(self.val, self.next)

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None
        left, right = 0, len(lists) - 1
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = mergeTwoLists(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]

list1 = ListNode(1)
list1.next = ListNode(3)
list2 = ListNode(2)
list2.next = ListNode(4)
list3 = ListNode(5)
list3.next = ListNode(6)
list4 = ListNode(7)
list4.next = ListNode(8)
print(Solution().mergeKLists([list1, list2, list3, list4]))

######################################################
# solution 2
######################################################
# from Queue import PriorityQueue

# def mergeklist(lists):
# 	q = PriorityQueue()
# 	head = curr = ListNode(0)
# 	for _list in lists:
# 		if _list:
# 			q.put((_list.val, _list))
# 	while not q.empty():
# 		val, node = q.get()
# 		curr.next = ListNode(val)
# 		curr = curr.next
# 		node = node.next
# 		if node:
# 			q.put((node.val, node))
# 	return head

# def mergeklist_2(lists):
# 	# list1 + list2 = list1
# 	# list3 + list4 = list3
# 	# .......
# 	while len(lists) > 1:
# 		# till we get 1 list left.. 
# 		for i in range(0, len(lists)-1, 2):
# 			# call mergetwolinkedlist and return combined list
# 			def mergetwolinkedlist(p1, p2):
# 			    pr = curr = ListNode(0)
# 			    while p1 != None and p2 != None:
# 			        if p1.val < p2.val:
# 			            curr = p1
# 			            curr = curr.next
# 			            p1 = p1.next
# 			        else:
# 			            curr = p2
# 			            curr = curr.next
# 			            p2 = p2.next
# 			    if p1 != None:
# 			        curr.next = p1
# 			    elif p2 != None:
# 			        curr.next = p2
# 			    return pr
            

# mergeklist_2([1,2,3,4])

