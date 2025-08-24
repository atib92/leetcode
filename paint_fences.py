"""
Paint Fence
Solved
Medium
Topics
conpanies icon
Companies
You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

Every post must be painted exactly one color.
There cannot be three or more consecutive posts with the same color.
Given the two integers n and k, return the number of ways you can paint the fence.

 

Example 1:


Input: n = 3, k = 2
Output: 6
Explanation: All the possibilities are shown.
Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.
Example 2:

Input: n = 1, k = 1
Output: 1
Example 3:

Input: n = 7, k = 2
Output: 42
 

Constraints:

1 <= n <= 50
1 <= k <= 105
The testcases are generated such that the answer is in the range [0, 231 - 1] for the given n and k.
"""
from functools import cache
class Solution:
    def numWaysRecursive(self, n: int, k: int) -> int:
        """
        N length array
        k colors : 0,1,...k-1
        At each cell we have k options. n^k which can be memoized to n*k
        func(i,last,llast)
        But this still doesn't run at scale ! See the DP solution below.
        """
        @cache
        def _numWays(i, last, llast):
            #print(i, last, llast)
            if i == n:
                return 1
            else:
                ret = 0
                for kk in range(k):
                    if kk == last and kk == llast:
                        continue
                    else:
                        ret += _numWays(i+1, kk, last)
                return ret
        _numWays.cache_clear()
        return _numWays(0,None,None)
    def numWays(self, n: int, k: int) -> int:
        """
        Lets thin of a DP approach:
        Lets define dp[i] as the number of ways to paint till fence index #i
        dp[0] = k 
        dp[1] = k
        From index #2 onwards there are two options for painting fence #i
        Option1 : Pick any color differnet from i-1 : k-1 X dp[k-1]
        Option2 : Pick the same color as i-1 but then you need to pick
                  any color different from i-2 : k-1 X dp[k-2]
        Add both the options:
        Time : O(N)
        Space : O(N)
        """
        if n < 2:
            return pow(k,n)
        dp = [0] * n
        dp[0] = k
        dp[1] = k*k
        for i in range(2,n):
            dp[i] = (k-1)*(dp[i-1]+dp[i-2])
        return dp[-1]
