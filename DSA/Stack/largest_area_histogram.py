# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
"""
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    index = 0
    n = len(heights)

    while index < n:
        print("stack: ", stack)
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
            print("if block: ", stack, index)
        else:
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = heights[top] * width
            max_area = max(max_area, area)
            print("else block: ", stack, top, width, area)

    while stack:
        top = stack.pop()
        width = index if not stack else index - stack[-1] - 1
        area = heights[top] * width
        max_area = max(max_area, area)
        print("while block: ", stack, top, width, area)

    return max_area


"""
Dry run:

Step  Index  Action             Stack       Max Area
0     0      push               [0]         0   
1     1      pop (0), push      [1]         2   
2     2      push               [1, 2]      2
3     3      push               [1, 2, 3]   2
4     4      pop (3,2), push    [1, 4]      10
5     5      push               [1, 4, 5]   10
End          pop (5,4,1)        []          10

"""


"""
A monotonic stack is:
	•	Monotonically Increasing → each new element is greater than the one below it
	•	Monotonically Decreasing → each new element is smaller than the one below it

The stack is called “monotonic” because the elements in it always maintain non-increasing or non-decreasing order.

Used to solve problems where you need to find the next/previous greater or smaller element in a sequence efficiently — typically in O(n) time.

Typical problems:
	•	Next Greater Element / Next Smaller Element
	•	Largest Rectangle in Histogram
	•	Daily Temperatures
	•	Trapping Rain Water
	•	Stock Span Problem
"""