# https://leetcode.com/problems/trapping-rain-water/
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right_max, left_max = [], []

        for i in range(len(height)):
            left_max.append(max(height[:i + 1]))

        for j in range(len(height)):
            right_max.append(0)
        for ind in range(len(height) - 2, -1, -1):
            right_max[ind] = max(height[ind:])

        final_sum = 0
        for i in range(1, len(left_max) - 1):
            final_sum += abs(min(left_max[i], right_max[i]) - height[i])

        return final_sum


# Testcase1
#        left_max = [0,1,1,2,2,2,2,3,3,3,3,3]

#        right_max =[3,3,3,3,3,3,3,3,2,2,2,0]

#        min = [0,1,1,2,2,2,2,3,2,2,2,0]

#        height = [0,1,0,2,1,0,1,3,2,1,2,1]

#        final = [0,0,1,0,1,2,1,0,0,1,0,0] => sum = 6

# Testcase2

#         left_max = [0,4,4,4,4,4]

#         right_max = [5,5,5,5,5,0]

#         min = [0,4,4,4,4,0]

#         height= [4,2,0,3,2,5]

#         final = [0,2,4,1,2,0] => sum = 9


#Solution 2
class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max, left_ind, right_max, right_ind, max_sum = height[0], 0, height[-1], len(height) - 1, 0
        for i in range(len(height)):
            if left_ind == right_ind:
                return max_sum

            if left_max > right_max:
                temp_sum = right_max - height[right_ind]
                right_ind -= 1
                right_max = max(right_max, height[right_ind])
            else:
                temp_sum = left_max - height[left_ind]
                left_ind += 1
                left_max = max(left_max, height[left_ind])

            max_sum = temp_sum + max_sum if temp_sum > 0 else max_sum


