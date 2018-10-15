
"""
Input:
2 -> number of input
L N K
2 3 4 
L : first lowercase letters. ex) 2 means a, b. 3 means a, b, c. 
N : length of words
K : Kth smallest palindromic word among all palindromic words

a, b
a, aa, aaa, aba, bab, bb, bbb (lexicographic order = dictionary order)

Output:
Case #1: 3
Case #2: 0

input example:
3 2 4
3 2 9
16 80 789862115964
21 58 857687157468
13 55 780298762474
6 83 641197618138

"""

class Solution(object):
    pass
            

if __name__ == '__main__':
    # words = ['aba', 'bab', 'bb', 'bbb', 'a', 'aa', 'aaa']
    # print(sorted(words))
    print(Solution().substring(['a', 'b']))