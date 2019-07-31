from __future__ import print_function

class Solution(object):
    def p(self,n):
        result_str = [""]*n*2
        _open = _close = 0
        return self.p_helper(result_str, n, 0, 0, 0)

    def p_helper(self,result_str, n, pos, _open, _close):
        if _close == n:
            for i in result_str:
                # Python 3.x expression but if you add
                # from __future__ import print_function, it works on Python 2.7 also
                print(i, end = "") 
            print()
        else:
            if _open > _close:
                result_str[pos] = ')'
                print("a",result_str)
                self.p_helper(result_str, n, pos+1, _open, _close+1)
            if _open < n:
                result_str[pos] = '('
                print("b",result_str)
                self.p_helper(result_str, n, pos+1, _open+1, _close)

Solution().p(3)
