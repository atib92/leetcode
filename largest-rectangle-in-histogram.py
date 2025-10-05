"""
Largest Rectangle in Histogram
Solved
Hard
Topics
conpanies icon
Companies
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # sentinel to flush stack
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                popped_index = stack.pop()
                height_at_popped = heights[popped_index]
                width = i if not stack else i - stack[-1] - 1 # **
                max_area = max(max_area, height_at_popped * width)
            stack.append(i)
        return max_area
