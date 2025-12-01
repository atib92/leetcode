"""
Find Maximum Balanced XOR Subarray Length
Solved
Medium
Topics
Hint
Given an integer array nums, return the length of the longest subarray that has a bitwise XOR of zero and contains an equal number of even and odd numbers. If no such subarray exists, return 0.

 

Example 1:

Input: nums = [3,1,3,2,0]

Output: 4

Explanation:

The subarray [1, 3, 2, 0] has bitwise XOR 1 XOR 3 XOR 2 XOR 0 = 0 and contains 2 even and 2 odd numbers.

Example 2:

Input: nums = [3,2,8,5,4,14,9,15]

Output: 8

Explanation:

The whole array has bitwise XOR 0 and contains 4 even and 4 odd numbers.

Example 3:

Input: nums = [0]

Output: 0

Explanation:

No non-empty subarray satisfies both conditions.

 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
"""
class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        stateMap = {(0,0):-1} # This is important when the valid window starts at the index 0
        res = 0
        xor, delta = 0,0
        for index, num in enumerate(nums):
            xor = xor ^ num
            if num % 2 == 0:
                delta += 1
            else:
                delta -= 1
            state = (xor, delta)
            if state in stateMap:
                # the window starts from previous stateMap[state] + 1 hence we do not do +1 in the index-stateMap[state] step next
                res = max(res, index-stateMap[state])
            else:
                stateMap[state] = index
        return res
