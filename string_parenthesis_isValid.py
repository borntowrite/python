# Given a string containing just the characters 
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

def is_valid_Parentheses(s):
    stack = []
    _dict = {
    	"]":"[", 
    	"}":"{", 
    	")":"("
    }
    for char in s:
        if char in _dict.values():
            stack.append(char)
        elif char in _dict.keys():
            if stack == [] or _dict[char] != stack.pop():
                return False
        else:
            return False
    return True

print(is_valid_Parentheses("()"))
print(is_valid_Parentheses("()[]{}"))
print(is_valid_Parentheses("(]"))
print(is_valid_Parentheses("([)]"))
print(is_valid_Parentheses("(()[])"))
print(is_valid_Parentheses(')') )