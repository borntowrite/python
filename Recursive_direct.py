# Recursion Variations
# - Direct
# - Indirect
# - Nested
# - Excessive
# - Tail

def factorial(total, n):
    if n == 0:
        total = 1
        print("      "*(4-n), total)
        return total
    print("      "*(4-n), "{}  *  factorial({}, {})".format(n, total, n-1))
    return factorial(total, n-1)*n

print(factorial(1,4))