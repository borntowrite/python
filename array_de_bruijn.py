
""" leetcode solution """
class Solution(object):
    # n: length
    # k: alphabet
    def DeBruijn(self, n, k):
        seen = set()
        answer = []
        try:
            alphabet = list(map(str, range(k)))
        except(ValueError, TypeError):
            alphabet = k
        def dfs(node):
            # map(function_to_apply, list_of_inputs)
            for x in alphabet:
                neighbor = node + x 
                if neighbor not in seen:
                    seen.add(neighbor) 
                    dfs(neighbor[1:]) 
                    answer.append(x) # Adding End Num
        dfs(alphabet[0] * (n-1))
        # print(seen)
        return "".join(answer) + alphabet[0] * (n-1)

print(Solution().DeBruijn(3,2))
print(Solution().DeBruijn(3,"ab"))

"""
[answer --> 00111010] + ["0"*(n-1) --> 00] = 
0011101000
000
 011
  111
   110
    101
     010
      100
       000
"""

""" wikipedia solution """

def de_bruijn(n, k):
    """
    de Bruijn sequence for alphabet k
    and subsequences of length n.
    """
    try:
        # let's see if k can be cast to an integer;
        # if so, make our alphabet a list
        _ = int(k)
        alphabet = list(map(str, range(k)))

    except (ValueError, TypeError):
        alphabet = k
        k = len(k)

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return "".join(alphabet[i] for i in sequence)

print(de_bruijn(3, 2))
"""
00010111 + 00 
000
 001
  010
   101
    011
     111
      110
       100
 
"""
print(de_bruijn(2, "abcd"))