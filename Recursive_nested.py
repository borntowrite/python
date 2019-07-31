# Recursion Variations
# - Direct
# - Indirect
# - Nested
# - Excessive
# - Tail

# Ackermann function - wilhelm Ackermann(1928) created this
# A(n,m) = m + 1             if n=0
#          A(n-1, 1)         if n>0, m=0
#          A(n-1, A(n,m-1))  if n,m>0

def ackermann(n,m):
    if n==0:
        print("1---",m,n)
        return m+1
    elif n>0 and m==0:
        print("2---",m,n)
        return ackermann(n-1,1)
    elif n>0 and m>0:
        print("3---",m,n)
        return ackermann(n-1, ackermann(n,m-1))

print(ackermann(1,2))
