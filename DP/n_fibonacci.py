# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        f_seq = [0, 1, 1]

        while len(f_seq) <= n:
            f_seq.append(sum(f_seq[-3:]))
        return f_seq[n]
