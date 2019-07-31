class Solution1(object):
	def maxParenthesis(self,string):
		maxlen = 0
		if len(string) < 2: return False
		for j in range(len(string)):
			for i in range(j, len(string)):
				if self.isValid(string[j:i+1]):
					maxlen = max(maxlen, i-j+1)
		return maxlen

	def isValid(self,string):
		temp = []
		for i in range(len(string)):
			if string[i] == '(':
				temp.append('(')
			elif temp != []:
				temp.pop()
			else:
				return False
		return temp == []

print(Solution1().maxParenthesis("((((((()))"))
print(Solution1().maxParenthesis(")()())"))
print(Solution1().maxParenthesis(")"))
print(Solution1().maxParenthesis("("))
print(Solution1().maxParenthesis("()"))
print(Solution1().maxParenthesis("()("))
print(Solution1().maxParenthesis("()()"))
print(Solution1().maxParenthesis("(()())"))

class Solution2(object):
	def longestValidParentheses(self,s):
		longest, last, temp = 0, -1, []
		for i in range(len(s)):
			if s[i] == '(':
				temp.append(i)
			elif not temp:
				last = i
			else:
				temp.pop()
				if not temp:
					longest = max(longest, i - last)
				else:
					longest = max(longest, i - temp[-1])
		return longest

print(Solution2().longestValidParentheses("(()())"))
print(Solution2().longestValidParentheses(")"))
