""" You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    """ DP : Bottoms Up 
    Also check coins.py for an interesting twist !
    """
    def climbStairs(self, n: int) -> int:
        dp = [1,1,2] + [0]*(n-2)
        for level in range(3,n+1):
            for step in range([1,2]):
                dp[level] += dp[level-step]
        return dp[n]
