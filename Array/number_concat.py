# https://leetcode.com/problems/largest-number/

"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

[1, 2, 3, 4] => 4321
[5, 508, 56] => 565508
[4, 5, 1] => 541

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            return -1 if a + b > b + a else 1

        nums_str = list(map(str, nums))
        res = sorted(nums_str, key=cmp_to_key(compare))
        res = "".join(res)
        return res if res[0] != '0' else '0'


# using plain sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]
        nums_str.sort(key=lambda a: a * 10, reverse=True)

        # Handle the case where the largest number is zero
        if nums_str[0] == "0":
            return "0"

        # Concatenate sorted strings to form the largest number
        return "".join(nums_str)



"""
Learnings:
https://www.geeksforgeeks.org/python/how-does-the-functools-cmp_to_key-function-works-in-python/
Python’s built-in sort() or sorted() no longer support custom comparators directly (since Python 3). 
Instead, you need to convert your comparator to a key function using functools.cmp_to_key.

Comparator return rules:
Syntax
    functools.cmp_to_key(func)

Parameter: func is a comparison function that takes two arguments and returns:
    - a negative number if the first argument is less than the second,
    - zero if they are equal,
    - a positive number if the first is greater than the second.

Returns: A callable object that can be used as a key function for sorting.
"""