"""
Product of Array Except Self
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ 
        First Pass, L2R[i] : Product of all elements from 0 to i-1
        Second Pass, R2L[i] : Product of all elements from N-1 to i+1
        Third Pass: output[i] = L2R[i]*R2L[i]
        Time O(N) space O(N)
        """
        N = len(nums)
        L2R = [1] * N
        R2L = [1] * N
        output = []
        for i in range(1,N):
            L2R[i] = L2R[i-1] * nums[i-1]
        for i in range(N-2,-1,-1):
            R2L[i] = R2L[i+1] * nums[i+1]
        for i in range(N):
            output.append(R2L[i]*L2R[i])
        return output
