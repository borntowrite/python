
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
            if s[left] != s[right]:
                return False
            left -= 1
            right += 1
        return True

print(Solution().isPalindrome("abcba")==True)
print(Solution().isPalindrome("abba")==True)
print(Solution().isPalindrome("abbac")==False)
print(Solution().isPalindrome("a")==True)
print(Solution().isPalindrome("")==False)

###################################################
# Palindrome using number and reverse
###################################################
class Solution2(object):
    def palindrome_num(self,num):
        reverse = 0
        original = num
        while num > 0 :
            reverse = reverse*10 + num%10
            num = num//10
            # print(num, reverse)
        # print("original {} = reverse {}".format(original, reverse))
        if original == reverse:
            return True
        else:
            return False

print(Solution2().palindrome_num(123321)==True)
print(Solution2().palindrome_num(12331)==False)

###################################################
# Palindrome very simple brute-force
###################################################
class Solution3(object):
    def palindrome_str(self, string):
        length = int(len(string)/2)
        for i in range(length):
            if string[i] != string[len(string)-1-i]:
                return False
        return True

print(Solution3().palindrome_str("abcba")==True) #odd
print(Solution3().palindrome_str("abccba")==True) #even
print(Solution3().palindrome_str("abccbaa")==False) 

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

class Solution4(object):
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
print(Solution4().palindrome_linkedlist(head)==False)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(Solution4().palindrome_linkedlist(head)==True)

head = ListNode(1)
print(Solution4().palindrome_linkedlist(head)==True)

c = ListNode(1)
c.add(1)
c.add(3)
c.add(2)
c.add(1)
# c.printTree()
print(Solution4().palindrome_linkedlist(c)==False)