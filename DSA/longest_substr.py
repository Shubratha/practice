# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# 1. Using set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


# 2. Using dict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        max_len, start = 0, 0
        for i, char in enumerate(s):
            if char_dict.get(char) is not None and char_dict[char] >= start:
                start = char_dict[char] + 1

            char_dict[char] = i
            max_len = max(max_len, i - start + 1)

        return max_len


