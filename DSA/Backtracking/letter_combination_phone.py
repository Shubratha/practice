# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example2:
Input: digits = ""
Output: []

Example3:
Input: digits = "2"
Output: ["a", "b", "c"]
"""

from typing import List

class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        phone_map = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                     "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        res = []

        if len(digits) <= 1:
            return phone_map.get(digits, [])

        def backtrack(index: int, path: list):
            if index == len(digits):
                res.append("".join(path))
                return

            letters = phone_map[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return res

