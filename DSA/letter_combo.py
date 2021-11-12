# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import itertools


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                   "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        ans = []
        if not digits:
            return ans
        if len(digits) == 1:
            return letters[digits]

        for combo in itertools.product(*[letters[k] for k in digits]):
            ans.append("".join(combo))
        print(ans)
        return ans
