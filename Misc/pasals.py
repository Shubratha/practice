# https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        res = [1,1]
        for i in range(rowIndex-1):
            left, right = 0, 0
            while right < len(res):
                left, res[right] = res[right], res[right] + left
                print(res)
                right+=1
            res.append(1)
        return res