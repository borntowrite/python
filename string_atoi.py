class Solution(object):
	def atoi(self, str):
		temp = 0
		for i in range(len(str)):
			temp += (ord(str[i])-48) * (pow(10, len(str)-1-i)) 
		return temp

print(Solution().atoi("1234"))
