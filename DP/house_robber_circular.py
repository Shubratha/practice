# https://leetcode.com/problems/house-robber-ii/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_rob1, max_rob2, rob1, rob2 = 0, 0, 0, 0
        # if len(nums) == 1:
        #     return nums[0]
        if len(nums) <= 3:
            return max(nums)
        print(nums[:-1])
        for h in nums[:-1]:
            rob = max(h+rob1, rob2)
            rob1 = rob2
            rob2 = rob
            max_rob1 = rob2
        rob1, rob2 = 0, 0
        for h in nums[1:]:
            rob = max(h+rob1, rob2)
            rob1 = rob2
            rob2 = rob
            max_rob2 = rob2
        return max(max_rob1, max_rob2)


"""
Test cases:
1) nums = [2,3,2] => 3
2) nums = [1,2,3,1] => 4
3) nums = [1,2,3] => 3
4) nums = [1] => 1
"""
