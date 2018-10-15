#############################################
# find the number of 1s in the binary representation of a number
#############################################
def findones(x):
	sum = 0
	while x > 0:
		sum = sum + (x & 1)
		x = x >> 1
	return sum

print(bin(1234))
print(findones(1234))
