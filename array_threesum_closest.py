def threesumClosest(nums, target):
    temp=[]
    distance=0
    d={}
    for i in range(len(nums)):
        left = nums[:i]
        right = nums[i+1:]
        current = nums[i]
        rest = left+right
        ret = twocombo(rest)
        for c in ret:
            temp.append([current]+c)
    # print(temp)
    distance = abs(target-sum(temp[i]))
    for i in range(1, len(temp)):
        # print(target, sum(temp[i]), abs(target-sum(temp[i])))
        if distance > abs(target-sum(temp[i])):
            distance = abs(target-sum(temp[i]))
            d.update({distance : sum(temp[i])})
    return d[distance]

def twocombo(rest):
    temp = []
    for i in range(len(rest)):
        for j in range(i, len(rest)):
            if i != j:
                temp.append([rest[i]]+[rest[j]])
    return temp

import time
from datetime import datetime
t_start = time.time()
print("closest number", threesumClosest([-4, -1, 1, 2], 1))
t_end = time.time() 
print("Total Time = ", t_end-t_start)

# Time:  O(n^2)
# Space: O(1)

# Given an array S of n integers,
# find three integers in S such that the sum is closest to a given number,
# target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, result, min_diff, i = sorted(nums), float("inf"), float("inf"), 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    diff = nums[i] + nums[j] + nums[k] - target
                    if abs(diff) < min_diff:
                        min_diff = abs(diff) # diff is lower then previous diff hence replace
                        result = nums[i] + nums[j] + nums[k]
                    if diff < 0: # means 3 sum is too low hence move j to higher number
                        j += 1
                    elif diff > 0: # means 3 sum is too high hence move k to lower number
                        k -= 1
                    else:
                        return target
            i += 1
        return result

s = Solution()
print(s.threeSumClosest([-4, -1, 1, 2], 1))




