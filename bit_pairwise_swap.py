
print(bin(0x55555555))
print(bin(0xaaaaaaaa))

def pairwise_swap(x):
    #return ((x >> 1)& 0x55555555 | (x << 1) & 0xffffffff)
    return (((x & 0x55555555) >> 1) | ((x & 0xffffffff) << 1))
print(pairwise_swap(1234))
print(bin(1234))
print(bin(2988))
