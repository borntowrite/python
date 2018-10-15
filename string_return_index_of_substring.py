class Solution(object):
	# """docstring for ClassName"""
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg

	def strstr(self, string, sub):
		index, i, j = -1, 0, 0

		while i < len(string):
			while j < len(sub):
				if string[i] == sub[j]:
					# print("string[{}]->{} = sub[{}]->{}, index={}".format(i, string[i], j, sub[j], i))
					if index < 0:
						index = i
					i += 1
					j += 1
				else:
					break
			i += 1
		if index >= 0:
			return index
		else:
			return -1

print(Solution().strstr("hello", "ll"))
print(Solution().strstr("aaaaa", "bba"))
print(Solution().strstr("abxyzcd", "xyz"))

