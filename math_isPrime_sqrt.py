import math

# print(int(math.sqrt(7)))
# print(math.sqrt(7))

def isPrime(n):
    if(n<2): return False
    elif(n==2): return True
    elif(n==3): return True
    elif(n%2==0): return False
    elif(n%3==0): return False

    return True

i=0
for i in range(20):
    if isPrime(i):
        print(i, "------ Prime Number")
    else:
        print(i, isPrime(i))
