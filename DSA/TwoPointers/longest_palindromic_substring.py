# https://leetcode.com/problems/longest-palindromic-substring

"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

# REF: https://youtu.be/aMH1eomKCmE

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        def get_palindrome_len(input_str, left, right):
            while left >= 0 and right < n and input_str[left] == input_str[right]:
                left -= 1
                right += 1
            return right - left - 1

        start, end = 0, 0

        # for each character in the str, find palindromic str by checking neighboring char
        for i in range(n):
            # check odd len palindromic str  Eg: aba
            odd = get_palindrome_len(s, i, i)
            # check even len palindromic str  Eg: abba
            even = get_palindrome_len(s, i, i + 1)
            max_len = max(odd, even)

            if max_len > end - start:
                # derive start and end indexes of palindrome
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start: end + 1]
