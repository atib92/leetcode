"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""
class Solution:
    cache = {}
    def rob(self, nums: List[int]) -> int:
        self.cache = {}
        self.nums = nums
        self.N = len(nums)
        return self._rob(0)
    def _rob(self, index):
        if index >= self.N:
            return 0
        ret = self.cache.get(index, None)
        if ret is None:
            a = self.nums[index] + self._rob(index+2)
            b = self._rob(index+1)
            self.cache[index] = max(a,b)
        return self.cache.get(index)

"""
EDIT: Check house_robbery_I for a much better DP approach with explanation.
"""
