from operator import add, sub, mul, truediv
from fractions import Fraction

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return nums[0] == 24
        ops = [add, sub, mul, truediv]
        for i in xrange(len(nums)):
            for j in xrange(len(nums)):
                if i == j:
                    continue
                next_nums = [nums[k] for k in xrange(len(nums)) if i != k != j]
                # for k in range(len(nums)):
                #     if i != k != j:
                #         next_nums = nums[k]
                for op in ops:
                    if ((op is add or op is mul) and j > i) or (op == truediv and nums[j] == 0):
                        continue
                    next_nums.append(op(nums[i], nums[j]))
                    if self.judgePoint24(next_nums):
                        return True
                    next_nums.pop()
        return False

s = Solution()
print(s.judgePoint24([4, 1, 8, 7]))
