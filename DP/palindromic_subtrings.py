# https://leetcode.com/problems/palindromic-substrings

"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

# two-pointers solution [O(N^2)]:
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        def expand(left, right):
            nonlocal ans
            while 0 <= left and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)  # odd
            expand(i, i+1)  # even

        return ans


# DP solution [O(N^2)]:
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [[False]* n for _ in range(n)]

        for l in range(1, n+1):
            for i in range(n-l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    if l == 1 or l == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    if dp[i][j]:
                        ans += 1
        return ans
