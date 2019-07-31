
"""
using dictionary 
"""
class Solution1(object):
    def is_valid_Parentheses(self,s):
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

print(Solution1().is_valid_Parentheses("()")==True)
print(Solution1().is_valid_Parentheses("()[]{}")==True)
print(Solution1().is_valid_Parentheses("(]")==False)
print(Solution1().is_valid_Parentheses("([)]")==False)
print(Solution1().is_valid_Parentheses("(()[])")==True)
print(Solution1().is_valid_Parentheses(')')==False)

"""
using stack
"""
class Solution2(object):
    def isValidParen(self, string):
        stack = []
        index = 0
        is_balanced = True
        while index < len(string) and is_balanced != False:
            paren = string[index]
            if paren in "([{":
                stack.append(paren)
            else:
                if stack == []:
                    is_balanced = False
                else:
                    top = stack.pop()
                    if not self.isValid(paren, top):
                        is_balanced = False
            index += 1
        if stack == [] and is_balanced == True:
            return True
        else:
            return False
    
    def isValid(self,close,open):
        if close == "}" and open == "{":
            return True
        elif close == "]" and open == "[":
            return True
        elif close == ")" and open == "(":
            return True
        else:
            return False

print("-----")
print(Solution2().isValidParen("()")==True)
print(Solution2().isValidParen("()[]{}")==True)
print(Solution2().isValidParen("(]")==False)
print(Solution2().isValidParen("([)]")==False)
print(Solution2().isValidParen("(()[])")==True)
print(Solution2().isValidParen(')')==False)
                    

