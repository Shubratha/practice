# https://leetcode.com/problems/first-missing-positive/

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_nums, max_nums = min(nums), max(nums)
        if min_nums > 0 and min_nums != 1:
            return 1
        if max_nums < 0:
            return 1

        unique_nums = set()
        for i in nums:
            if i > 0:
                unique_nums.add(i)
        i = 1
        while True:
            if i in unique_nums:
                i += 1
            else:
                return i
