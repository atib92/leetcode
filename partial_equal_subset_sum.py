"""
416. Partition Equal Subset Sum
Solved
Medium
Topics
Companies
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        The idea is very simple.
        a. If the total sum of the input array is odd, there is no way we can have two equal subset arrays. So return False.
        b. If the total sum is even, then the problem simply becomes to find a subset with target sum = toal sum / 2
        To solve b. You can solve it using recursios (def find) but this O(2^N) or solve it using knapsack wihch is O(N^2)
        """
        @cache
        def find(index, target):
            if target == 0:
                return True
            else:
                if index >= n or target < 0:
                    return False
                else:
                    skip = find(index+1, target)
                    keep = find(index+1, target-nums[index])
                    return skip or keep
        def findKnapSack(nums, target):
            dp = [[False]*(target+1) for _ in range(len(nums)+1)] # Adding a dummy first row
            for index in range(len(nums)+1):
                dp[index][0] = True
                for w in range(1, target+1):
                    skip = dp[index-1][w]
                    keep = dp[index-1][w-nums[index-1]] if w >= nums[index-1] else False
                    dp[index][w] = skip or keep
            return dp[len(nums)][w]
        s = 0
        n = len(nums)
        for i in range(n):
            s += nums[i]
        if s % 2 != 0:
            # Odd sum
            return False
        else:
            target = s // 2
            #ret = find(0, target)
            #find.cache_clear()
            ret = findKnapSack(nums, target)
            return ret
