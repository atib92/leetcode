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
    def numDistinctRecursive(self, s: str, t: str) -> int:
        """
        subsequences of s which equals t
        rabbbit rabbit
        i       j
        Keep two points i,j
        if s[i] == s[j] 
            Recurse twice :
            1. Include s[i] so i+=1 and j+=1
            2. Skip s[i] so just i+= 1 (we want some other s[i] to match t[j])
        else:
            same as #2 (no other option)
        Everytime we reach j == len(t), we have completed j so 
        Complexity: 2^N (two options for each letter in s) 2^1000 is too bad !!
        But you can memoize the same <i,j> combination and make it O(N*M)
        """
        @cache
        def _numDistinct(i, j):
            if j == M:
                return 1
            elif i < N and j < M:
                ret = 0
                if s[i] == t[j]:
                    # include
                    ret  += _numDistinct(i+1, j+1)
                # skip
                ret += _numDistinct(i+1, j)
                return ret
            else:
                return 0
        N, M = len(s), len(t)
        return _numDistinct(0,0)
    def numDistinct(self, s: str, t: str) -> int:
        """
        A bottoms up DP approach. We define dp[i][j] as the number of distinct
        subsequences of of s[:i] that matches t[:j]. This organically forces you
        to create a N+1 X M+1 array and bootstrap it by setting dp[0][0] = 1
        """
        N, M = len(s), len(t)
        dp = [[0]*(M+1) for _ in range(N+1)]
        dp[0][0] = 1
        for i in range(1, N+1):
            for j in range(M+1):
                if j > i:
                    # Optimization: A shorter s' can never match t'
                    continue
                dp[i][j] += dp[i-1][j]
                if j > 0 and s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[N][M]
"""
Complexity
Time complexity:
O(N*M)
Space complexity:
O(N*M)
"""
