def maxParenthesis(string):
	maxlen = 0
	if len(string) < 2: return False
	for j in range(len(string)):
		for i in range(j, len(string)):
			if isValid(string[j:i+1]):
				maxlen = max(maxlen, i-j+1)
	return maxlen

def isValid(string):
	temp = []
	for i in range(len(string)):
		if string[i] == '(':
			temp.append('(')
		elif temp != []:
			temp.pop()
		else:
			return False
	return temp == []

print(maxParenthesis("((((((()))"))
print(maxParenthesis(")()())"))
print(maxParenthesis(")"))
print(maxParenthesis("("))
print(maxParenthesis("()"))
print(maxParenthesis("()("))
print(maxParenthesis("()()"))
print(maxParenthesis("(()())"))

def longestValidParentheses(s):
    longest, last, temp = 0, -1, []
    for i in xrange(len(s)):
        if s[i] == '(':
            temp.append(i)
        elif not temp:
        	print("comming?")
        	last = i
        else:
            temp.pop()
            if not temp:
                longest = max(longest, i - last)
            else:
                longest = max(longest, i - temp[-1])
    return longest

print(longestValidParentheses("(()())"))
print(longestValidParentheses(")"))
