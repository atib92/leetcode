""" Given an integer array nums, find the  subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6."""

class Solution:
    """ 
    _max_here_ : Max sum subarray that ends at index 'i'
    _max_ : Running maximum of _max_here_
    Algorithm : The idea is to use the last _max_here (i,e at index:i-1) and make a decision if _max_here at index:i should
    continue to subarray or not. The decision boils down to:
    a. If _max_here_ is +ve, we should extend the subarray.
    b. if _max_here_ is -ve, including it will reduce the subarray sum of subarray ending at 'i'
    Demonstration:
    nums:     [-2, 1, -3, 4,-1, 2, 1,-5, 4]
    _max_here: -2, 1, -2, 4, 3, 5, 6, 1, 5
    _max_ :    -2, 1,  1, 4, 4, 5, 6, 6, 6
    """
    def maxSubArray(self, nums: List[int]) -> int:
        _max_, _max_here_ = nums[0], nums[0]
        for num in nums[1:]:
            _max_here_ = max(num, num+_max_here_)
            _max_ = max(_max_, _max_here_)
        return _max_
