"""
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.

"""
class Solution:
    """
    Algo:
    1. Create an array max_right (left to right) which stores the maximum num seen coming from right.
    2. For any pair (i, j) if nums[i] <= max_right[j] we can say for sure that there is atleast a ramp starting  at 'i' and ending at >= 'j'. Check for larger ramps in j++ direction
    3. For any pair (i, j) if nums[i] > max_right[j] we can say for sure there is no value in index >= 'j' that is greater than nums[i] so no ramp possible. Check for smaller ramps starting from i++
    """
    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        Sliding window after pre-processing
        """
        N = len(nums)
        max_right = [-100000] * N
        max_right[-1] = nums[-1]
        max_ramp = 0
        # PreProcessing
        for i in range(N-2,-1,-1):
            max_right[i] = max(max_right[i+1], nums[i])
        l,r = 0,0
        while(l < N and r < N and l <= r):
            if max_right[r] >= nums[l]:
                max_ramp = max(max_ramp, r - l)
                r += 1
            else:
                l += 1
                r += 1 # This is an awesome hack because even if we can create a ramp afer l++ it would still be smaller than the prev.
                       # ramp size if r is not incremented.
        return max_ramp
