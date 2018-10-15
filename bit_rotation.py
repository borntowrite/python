def bit_rotate(x, n):
	print(bin(x))
	return (x >> n | x << (32-n))

print(bin(bit_rotate(9, 3)))


