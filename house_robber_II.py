"""
House Robber II
Solved
Medium
Topics
conpanies icon
Companies
Hint
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

class Solution:
    """
    Check house_robber_1.py
    This is very similar to the linear case. The only addition here is that i=0 and i=N-1 are
    considered adjacent. To solve this, we simply break the circle and think of two house_robber_I problem:
    i. From index 0 to N-2
    ii. From index 1 to N-1
    and return the max of the two.
    """
    def rob(self, nums: List[int]) -> int:
        def _rob(arr: List[int]) -> int:
            state = (0, arr[0])
            n = len(arr)
            i = 1
            while(i < n):
                pick = state[0] + arr[i]
                skip = max(state[1], state[0])
                state = (skip, pick)
                i += 1
            return max(state)
        if len(nums) <= 1:
            return sum(nums)
        return max(_rob(nums[:-1]), _rob(nums[1:]))
        
