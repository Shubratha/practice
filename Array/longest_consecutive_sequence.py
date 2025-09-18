# https://leetcode.com/problems/longest-consecutive-sequence/

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List


#  O(n) time
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for n in num_set:
            if n-1 not in num_set:
                cur = n
                cur_len = 1
                while cur + 1 in num_set:
                    cur += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)

        return max_len



# O(n log n) with sorting
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))  # remove duplicates and sort
        max_len = cur_len = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 1

        return max_len
