'''
3Sum Closest
Solved
Medium
Topics
conpanies icon
Companies
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        delta = float('inf')
        closest_sum = None
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum == target:
                    return target
                else:
                    if abs(current_sum - target) < delta:
                        delta = abs(current_sum - target)
                        closest_sum = current_sum
                    if current_sum > target:
                        r -= 1
                    else:
                        l += 1
        return closest_sum
