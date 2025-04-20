"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Keeps a track of last insert non-zero elements and total count of zero elements. Traverse the array once and keep adding
        non zero elements from the left. Once done, just add zeros to the end in the right quantity.
        """
        last_insert = -1
        count_zeros = 0
        for index, elem in enumerate(nums):
            if elem == 0:
                count_zeros += 1
            else:
                last_insert += 1
                nums[last_insert] = elem
        while(count_zeros > 0):
            count_zeros -= 1
            last_insert += 1
            nums[last_insert] = 0
