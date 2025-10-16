"""
Max Consecutive Ones III
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        We maintain a sliding window from l_index to r_index and ensure we do not have more than k zeros.
        If at any time number of zeros exceeds k, shrink the window from the l_index until the number of
        zeros comes back to <= k
        """
        max_streak, l_index, r_index, n, zeros = 0, 0, 0, len(nums), 0
        while(l_index <= r_index and r_index < n):
            if nums[r_index] == 0:
                zeros += 1
                while(zeros > k):
                    if nums[l_index] == 0:
                        zeros -= 1
                    l_index += 1
            max_streak = max(max_streak, r_index-l_index+1)
            r_index += 1
        return max_streak
