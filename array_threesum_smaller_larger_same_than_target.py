
# condition1 : nums input must be more than 3 numbers
class Solution:
	def findCombo(self, nums, target):
		i = 0
		bigger = []
		smaller = []
		same = []
		while i < len(nums)-2:
			j = i+1
			k = len(nums)-1
			while j < k:
				if nums[i] + nums[j] + nums[k] < target:
					# smaller.append(set((nums[i], nums[j], nums[k])))
					smaller.append((nums[i], nums[j], nums[k]))
					j += 1
				elif nums[i] + nums[j] + nums[k] > target:
					# bigger.append(set((nums[i], nums[j], nums[k])))
					bigger.append((nums[i], nums[j], nums[k]))
					k -= 1
				else: # if it's same.. 
					# same.append(set((nums[i], nums[j], nums[k])))
					# same.append((nums[i], nums[j], nums[k]))
					j += 1
					k -= 1
			i += 1
		print("smaller than target = ", smaller)
		print("bigger than target = ", bigger)
		print("same as target = ", same)

s = Solution()
s.findCombo([3,1,4,6,2,-1,-2,7], 5)


					


		
