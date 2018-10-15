#######################################################
# write a function to determine the number of bits
# you would need to filp to convert integer A to integer B
#######################################################

def count(a, b):
	#print(b ^ 0xF) # all bit flip
	#print(~b & 0xF) # all bit flip
	#c = a & (b ^ 0xF) # this works but use below expressioin (XOR)
	c = a ^ b
	print(bin(c))
	n = number = 0
	while c != 0:
		if c & 1 == 1:
			print("if nth bit is 1")
			number += 1
		c = c >> 1
	return number

print("number of 1s = ", count(13, 8))

# print(int(0b1101))
# print(int(0b1000))