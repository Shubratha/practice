# https://leetcode.com/problems/jump-game-ii/

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r, jumps = 0, 0, 0
        while r < len(nums) - 1:
            max_reachable = 0
            # get max distance that can be covered for a position
            for i in range(l, r + 1):
                max_reachable = max(max_reachable, i + nums[i])

            # move the pointer to left most and right most of the possible distances
            l = r + 1
            r = max_reachable
            # increment jump
            jumps += 1
        return jumps


"""
Testcases:
Input: nums = [2,3,1,1,4]
Output: 2

Input: nums = [4,0,1,3]
Output: 1
"""