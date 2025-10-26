"""
Maximum Alternating Sum of Squares
Solved
Medium
Hint
You are given an integer array nums. You may rearrange the elements in any order.

The alternating score of an array arr is defined as:

score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...
Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.

 

Example 1:

Input: nums = [1,2,3]

Output: 12

Explanation:

A possible rearrangement for nums is [2,1,3], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = 22 - 12 + 32 = 4 - 1 + 9 = 12

Example 2:

Input: nums = [1,-1,2,-2,3,-3]

Output: 16

Explanation:

A possible rearrangement for nums is [-3,-1,-2,1,3,2], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = (-3)2 - (-1)2 + (-2)2 - (1)2 + (3)2 - (2)2 = 9 - 1 + 4 - 1 + 9 - 4 = 16

 

Constraints:

1 <= nums.length <= 105
-4 * 104 <= nums[i] <= 4 * 104
"""
"""
Approach
1. -ve numbers do not matter since we squares
2. Compute the square matrix
3. + - + - ... Comput the # of -ve (its is n//2)
4. Use the smallest n//2 from the squared matrix as the -ves
"""

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums_sqr = sorted([n*n for n in nums])
        minus = len(nums) // 2
        return -1*sum(nums_sqr[:minus]) + sum(nums_sqr[minus:])
