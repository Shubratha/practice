# https://leetcode.com/problems/palindrome-pairs/description/

"""
You are given a 0-indexed array of unique strings words.

A palindrome pair is a pair of integers (i, j) such that:

0 <= i, j < words.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a palindrome.
Return an array of all the palindrome pairs of words.

You must write an algorithm with O(sum of words[i].length) runtime complexity.



Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["a","a"]
"""
from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        indexed_words = {word: idx for idx, word in enumerate(words)}
        ans = []

        for idx, word in enumerate(words):
            for j in range(len(word) + 1):
                left_split_word = word[:j]
                right_split_word = word[j:]
                rev_left = left_split_word[::-1]
                rev_right = right_split_word[::-1]

                # Check if the reversed left part exists in the dictionary,
                # and the right part is a palindrome, also ensure it's not the same word.
                if rev_left in indexed_words and idx != indexed_words[rev_left] and rev_right == right_split_word:
                    ans.append([idx, indexed_words[rev_left]])

                # Check if the reversed right part exists in the dictionary, and
                # the left part is a palindrome, also ensure it's not the same word.
                # We also check j to ensure we do not double-count palindromes.
                if j > 0 and rev_right in indexed_words and idx != indexed_words[
                    rev_right] and rev_left == left_split_word:
                    ans.append([indexed_words[rev_right], idx])

        return ans