"""
two sum using hashmap (dict) 
Output: return index of two number 
"""
class Solution:
    def twoSum(self, nums, target):
        temp = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            print("{} = {} - nums[{}] => {}".format(remaining, target, i, nums[i]))
            if remaining in temp:
                return (temp.get(remaining), i)
            temp.update({nums[i]:i})
            print(temp)

print(Solution().twoSum([2,15,11,7], 18))
