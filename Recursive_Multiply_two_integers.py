
###########################################
# Recursive Multiplication
###########################################

def mul_recursive(small, big):
    if small ==0: return 0
    elif small ==1: return big
    s = small >>1
    print("call mul_recursive({}, {})".format(s, big))
    halfprod = mul_recursive(s, big)
    print("halfprod", halfprod, "small", small, "big", big)
    if small % 2 == 0: 
        print("return halfprod + halfprod", halfprod + halfprod)
        return halfprod + halfprod
    else: 
        print("return halfprod + halfprod + big", halfprod + halfprod + big)
        return halfprod + halfprod + big

print(mul_recursive(6,6))


###########################################
# Recursive Multiplication
# can't handle larger number - due to limited number of recursive call
###########################################
# from functools import lru_cache

# @lru_cache(maxsize=15)
# def multiply(x,y):
#     # add x with y times
#     print("x, y: ", x,y)
#     if(y == 0):
#         return 0
#     if(y > 0 ):
#         return (x + multiply(x, y - 1))
#     if(y < 0 ):
#         return -multiply(x, -y)

# print(multiply(10,10))
# print(multiply(10,-10))

###########################################
# Karatsuba Multiplication
# if number is huge, this algorithm is better
# ex)
# 1000 * 2000 = 2000000
# a1 = 10, a0 = 0
# b1 = 20, b0 = 0
# n = 4
# c = (a1*b1) * 10**n + (a1 * b0 + a0 * b1)* 10**(n/2) + (a0*b0)
# time complexity : O(n^log3) = O(n^1.585) < O(n^2)
###########################################

##So: what's the product of the following two 64-digit numbers?
##3141592653589793238462643383279502884197169399375105820974944592
##2718281828459045235360287471352662497757247093699959574966967627

# a1 = 31415926535897932384626433832795
# a0 = 2884197169399375105820974944592
# b1 = 27182818284590452353602874713526
# b0 = 62497757247093699959574966967627
# n = 64
# n2 = n/2

# c = (a1*b1) * 10**n + (a1 * b0 + a0 * b1)* 10**int(n/2) + (a0*b0)

# print(c)

