"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left_max, right_max = [0] * N, [0] * N
        water = 0
        for pos in range(1,N-1):
            left_max[pos] = max(left_max[pos-1], height[pos-1])
        for pos in range(N-2,0,-1):
            right_max[pos] = max(right_max[pos+1], height[pos+1])
        for pos in range(1,N-1):
            water += max(0,min(left_max[pos], right_max[pos]) - height[pos])
        return water
