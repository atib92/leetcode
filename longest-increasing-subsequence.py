"""
 Longest Increasing Subsequence
Solved
Medium
Topics
conpanies icon
Companies
Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
class Solution:
    def binary_insert(self, left, right, n):
        """
        Use this examples to verify why we return 'left'
        [1, 5, 6], 3 -> [1,3,6] Since 3 can extend [1] 
        [5, 7, 9], 6 -> [5,6,9] Since 6 can extend [5]
        [5, 7, 9], 8 -> [5,7,8] Since 8 can extend [5, 7]. Note any value which could have extended [5,7,9] will extend [5,6,8] as well so we are safe in overwriting 9
        """
        while left <= right:
            mid = (left + right) // 2
            if self.res[mid] == n:
                return
            elif self.res[mid] > n:
                right = mid - 1
            else:
                left = mid + 1        
        self.res[left] = n
        return

    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return N
        else:
            self.res = [nums[0]]
            m = 1 # We maintain the lenghth of res so that we do not have compute it every time we need to call binary_insert
            for i in range(1, N):
                if nums[i] > self.res[-1]:
                    # We can extend the last LIS safely
                    self.res.append(nums[i])
                    m += 1
                else:
                    # nums[i] cannot extend res[-1]
                    # We need to insert nums[i] in res[] such that a LIS res[... nums[i]] ends at nums[i]
                    # We need to find an index in res[j] s.t nums[i] > res[j] i,e it can extend res[j]
                    # a.k.a we need to insert nums[i] in res[].
                    # Ofcourse we can do that in O(N) but that is going to make the algo O(N^2)
                    # Since res[] is sorted, we can do that in O(logN) making the alog O(NlogN)
                    self.binary_insert(0, m-1, nums[i])
        return len(self.res) 
