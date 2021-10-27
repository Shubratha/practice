# https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable, flag = 0, True
        for i, num in enumerate(nums):
            if i > reachable:
                # index is beyond reachable distance
                flag = False
                break
            if reachable == len(nums) - 1:
                # reached the end
                break
            reachable = max(i + num, reachable)
        return flag


"""
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""