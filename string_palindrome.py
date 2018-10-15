
###################################################
# Palindrome using brute-force (from mid point)
###################################################
class Solution(object):
    def isPalindrome(self, s):
        if not s:
            return False
        if len(s)%2 == 0: # even case
            left = int(len(s)/2)-1
            right = left+1
        else: # odd case
            left = int(len(s)/2)
            right = int(len(s)/2)
        while left >= 0 and right < len(s):
            print("s[{}]={}, s[{}]={}".format(left, s[left], right, s[right]))
            if s[left] != s[right]:
                return False
            left -= 1
            right += 1
        return True
        
print(Solution().isPalindrome("abcba"))
print(Solution().isPalindrome("abba"))
print(Solution().isPalindrome("abbac"))
print(Solution().isPalindrome("a"))
print(Solution().isPalindrome(""))

###################################################
# Palindrome using stack
###################################################



###################################################
# Palindrome using number and reverse
###################################################
def palindrome_num(num):
	reverse = 0
	original = num
	while num > 0 :
		reverse = reverse*10 + num%10
		num = num/10
		print(num, reverse)
	print(original, reverse)
	if original == reverse:
		return True
	else:
		return False

print(palindrome_num(123321))

###################################################
# Palindrome very simple brute-force
###################################################
def palindrome_str(string):
	length = int(len(string)/2)
	for i in range(length):
		if string[i] != string[len(string)-1-i]:
			return False
	return True

print("abcba", palindrome_str("abcba")) #odd
print("abccba", palindrome_str("abccba")) #even
print("abccbaa", palindrome_str("abccbaa")) 

###################################################
# Palindrome using linkedlist
###################################################
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)

    def add(self, val):
        if self.next is None:
            self.next = ListNode(val)
        else:
            self.next.add(val)

    def printTree(self):
        print(self.val)
        if self.next:
            self.next.printTree()

class Solution2(object):
    def palindrome_linkedlist(self, head):
        stack = []
        slow = head
        fast = head
        # go to half only
        while fast and fast.next:
            stack.append(slow.val)
            # print(stack)
            fast = fast.next.next
            slow = slow.next
        # if length is odd, then one more to go
        # this is actually center of palindrome
        if fast:
            slow = slow.next  
        # iterate thru the rest half to see if it's same as first half
        while slow:
            if stack.pop() != slow.val: 
                # if pop value is different from slow val, then return false immediately 
                return False
            slow = slow.next
        return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(Solution2().palindrome_linkedlist(head))

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(Solution2().palindrome_linkedlist(head))

head = ListNode(1)
print(Solution2().palindrome_linkedlist(head))

c = ListNode(1)
c.add(1)
# c.add(3)
# c.add(2)
# c.add(1)
#c.printTree()
print(Solution2().palindrome_linkedlist(c))