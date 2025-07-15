"""
Longest Palindromic Subsequence
Solved
Medium
Topics
conpanies icon
Companies
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Top down DP:
        We iterate from i to j to find palindromic subsequences of differnent lengths.
        At every step we compute dp[i][j] using earlier valies.
        """
        n = len(s)
        dp = [[0]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i + 1 < n:
                dp[i][i+1] = 2 if s[i] == s[i+1] else 1
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j])
        ret = 0
        for i in range(n):
            for j in range(n):
                ret = max(ret, dp[i][j])
        return ret
