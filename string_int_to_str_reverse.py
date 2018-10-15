
a = 123
b = -123

def reverse_int(x):
    ret = 0
    num = x
    x = abs(x)
    while x != 0:
        pop = x % 10
        x = int(x/10)
        ret = ret*10 + pop
    if num < 0:
        return -ret
    elif num > 0:
        return ret

print(reverse_int(a))
print(reverse_int(b))

def reverse(x):
        num = 0
        a = abs(x)
        while(a != 0):
            pop = a % 10
            num = num * 10 + pop
            a = int(a / 10)
        if x > 0 and num < 2**31:
            return num
        elif x < 0 and num <= 2**31:
            return -num
        else:
            return 0

print(reverse(b))

# a = 123
# a_string = str(a)
# r_string = ""
# length = len(a_string)-1
# for i in range(len(a_string)):
#     r_string += a_string[length-i]
# print(r_string)


