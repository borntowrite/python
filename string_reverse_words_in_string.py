class Solution(object):
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))
        
if __name__ == '__main__':
    print(Solution().reverseWords('hello world'))

# print('#'.join("ya ya".split()))