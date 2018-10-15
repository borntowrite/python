
class Solution(object):
	def prefix(self, str):
		res = ""
		# find shortest string in array first
		shortest = float('inf')
		for i in range(len(str)):
			shortest = min(shortest, len(str[i]))

		for i in range(shortest):
			for j in range(1, len(str)):
				if str[0][i] == str[j][i]:
					if str[0][i] not in res:
						res += str[0][i]
				else:
					break
			if str[j][i] != str[0][i]:
				break
		return res

print(Solution().prefix(["hello", "heaven", "heavy"]))
print(Solution().prefix(["abcdddfsdfsfd", "abcdef", "abc"]))
