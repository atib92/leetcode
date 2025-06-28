"""
Distinct Subsequences
Solved
Hard
Topics
premium lock icon
Companies
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""
class Solution:
    def _numDistinct(self, i, j):
        if i >= self.S:
            return 1
        elif j >= self.T:
            return 0
        else:
            if self.memo[i][j] is None:
                ans = 0
                if self.s[i] == self.t[j]:
                    ans += self._numDistinct(i+1, j+1)
                ans += self._numDistinct(i, j+1)
                self.memo[i][j] = ans
            return self.memo[i][j]
    def numDistinct(self, t: str, s: str) -> int:
        """
        We use a bottom up recursive solution with caching.
        The idea is to find 't' in a subsequence of 's' so at
        any step we have two options:
        1. If s[i] == t[j], we can include s[i] and look for the remainder of t[j+1:] in s[i+1:]
        2. Skip s[i] and continue to look for t[j:] in s[i+1:]
        There will be repetetive calls for any (i, j) pair where caching is used.

        This can also be approached via a more convntional bottoms up DP approach where:
        dp[i][j] is the no. of ways to make t[:i] using s[:i] and we can extend this as follows:
        dp[i][j] = dp[i-1][j-1] * (s[i] == t[j] ? 1 : 0) + dp[i-1][j] 
        """
        self.s = s
        self.t = t
        self.S = len(s)
        self.T = len(t)
        self.memo = [[None] * 1000 for _ in range(1000)]
        return self._numDistinct(0,0)
