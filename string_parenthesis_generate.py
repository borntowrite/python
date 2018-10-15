from __future__ import print_function

def generateParenthesis(n):
    result_str = [""]*n*2
    pos = _open = _close = 0
    return _generateParenthesis(result_str, n, 0, 0, 0)

def _generateParenthesis(result_str, n, pos, _open, _close):
    if _close == n:
        for i in result_str:
            # Python 3.x expression but if you add
            # from __future__ import print_function, it works on Python 2.7 also
            print(i, end = "") 
        print()
    else:
        if _open > _close:
            result_str[pos] = ')'
            _generateParenthesis(result_str, n, pos+1, _open, _close+1)
        if _open < n:
            result_str[pos] = '('
            _generateParenthesis(result_str, n, pos+1, _open+1, _close)
        
generateParenthesis(3)
