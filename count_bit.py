
## Big O(n)
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

## Big O(n)
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

if __name__ == "__main__":
    print(count_bits(4)) #100
    print(count_bits(5)) #101
    print(parity(4))
    print(parity(5))

    a = [1,2,3,4,5,6,7]
    a[0], a[len(a)-1] = a[len(a)-1], a[0]
    print (a)
