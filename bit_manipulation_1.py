#########################
# divide by 2 
# shift 1 to right is same as divide by 2
#########################
x = 6
x = x >> 1 
print(x)

#########################
# Upper Case -> Lower Case w/ bitwise
#########################
# a << b = a * (2 ** b)
# a >> b = a // (2 ** b)
letr = ord('T') # 84 - ord() return unicode
print(bin(letr)) # 0b1010100 - 84 - 'T'
print(int(0b1110100)) # 0b1110100 - 116 - 't'
print(chr(116)) # 't'
conv = 32 # 0b100000
l_letr = chr(letr | conv) # if change 6th bit to 1, then upper case will become lower case
print(l_letr)

#########################
# bit shifter
#########################
def shift(x, count):
    for i in range(count):
        x = x << 1
    return x

print(shift(10, 5))

#########################
# even/odd 
#########################
def evenodd(x: int):
    if x & 1 == 0:
        print("even")
    else:
        print("odd")

evenodd(3)

#########################
# is_nth_bit_set
#########################
def is_nth_bit_set(x: int, n: int):
	if x & (1 << n):
		return True
	return False

print(is_nth_bit_set(6,2))

#########################
# set nth bit 
#########################
def set_nth_bit(x: int, n: int):
	a = x | (1 << n)
	b = bin(x | (1 << n))
	return a, b
print("6 to bin", bin(6))
print(set_nth_bit(6,0))
print(set_nth_bit(6,1))

#########################
# unset nth bit 
#########################
def unset_nth_bit(x: int, n: int):
	a = x ^ (1 << n)
	b = bin(x ^ (1 << n))
	return a, b
print("6 to bin", bin(6))
print(unset_nth_bit(6,0))
print(unset_nth_bit(6,1))

#########################
# toggle nth bit 
#########################

def toggle_nth_bit(x: int, n: int):
	a = x ^ (1 << n)
	b = bin(x ^ (1 << n))
	return a, b
print("6 to bin", bin(6))
print(toggle_nth_bit(6,0))
print(toggle_nth_bit(6,1))

