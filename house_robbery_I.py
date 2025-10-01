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
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
class Solution:
    """
    The idea is pretty simple, at point in time we have two options to rob a house or not
    but we use simple recursion, the time complexity will blow up to exponential. A much
    better (knapsack/dynamic programming) way of thinking about this problem is to define
    the dp state as dp[n][2] where dp[i][0] is the max amount we can rob till house #i
    if rob the ith house and dp[i][1] is the max amount we can rob till house #i if we skip
    house #i.
    With the notation out of the way, the state transtions looks like this:
    dp[i][1] = maximum amt that can be robbed if we rob house i = dp[i-1][0]
    dp[i][0] = maximum amt that can be robbed if we skip house i. This is interesting since
               we can continue the last robbed / skipped state depending on what gives
               us the maxiumu. We are not bound to continue only the last robbed state if the
               last skipped state gives us a better amount.
    Space Optimization: You don't really need the dp array, at any time you are only interested
    in the two values from the last index so a tuple suffices.

    Time: O(N)
    Space: O(1)
    """
    def rob(self, arr: List[int]) -> int:
        n = len(arr)
        if len(arr) <= 1:
            return sum(arr)
        else:
            state = (0, arr[0])
            i = 1
            while(i < n):
                pick = state[0] + arr[i]
                skip = max(state[1], state[0])
                state = (skip, pick)
                i += 1
            return max(state)


# Much Simpler DP
class Solution:  
    def findMaxSum(self, houses):
        n = len(houses)
        dp = [0] * n
        dp[0] = houses[0]
        if n > 1:
            dp[1] = max(dp[0], houses[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2]+houses[i])
        return dp[-1]
# OG
class Solution:  
    def findMaxSum(self, houses):
        n = len(houses)
        dp = [0] * (n+1)
        dp[1] = houses[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+houses[i-1])
        return dp[-1]
