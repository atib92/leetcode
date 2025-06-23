"""
 Subarray Sum Equals K
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
class Solution:
    def subarraySumBruteForce(self, nums: List[int], k: int) -> int:
        """
        The point to note here is that the subarrays can contain -ve numbers so the
        conventional sliding window woudn't work here.
        Time O(N^2)
        """
        count = 0
        n = len(nums)
        for start in range(n):
            s = 0
            for end in range(start, n):
                s += nums[end]
                if s==k:
                    count += 1
        return count
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Use a hashmap to store cumulative sums.
        Whenever you see a cumulative sum 's' if you know the number of times 's-k' was seen earlier, you know exactl that many time the sum 'k' can be made
        Time: O(N)
        """
        smap = {0:1} # This is to count  cases when there are individual elements = k in the array !
        s = 0
        count = 0
        for elem in nums:
            s += elem
            if s-k in smap:
                count += smap.get(s-k)
            smap[s] = smap.get(s, 0) + 1
        return count
