"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

class Solution:
    """
    Algo: The problem has both traits that make it solvable by Dynamic Programming.
    i. Optimal Substructure 
    ii. Overlapping Sub Problems
    LCS of (s1[i:], s2[j:]) can be solved by first solving (s1[i+1:], s2[j+1:]), (s1[i:], s2[j+1:]) and (s1[i+1:], s2[j:])
    Like any classic bottom up DP approach, there is also a top-down recursive approach. We also implement that with memoisation below.
    """
    def longestCommonSubsequence_DyanamicProgramming(self, text1: str, text2: str) -> int:
        """
        Bottoms-Up Dynamic Programming solution
        """
        L, M = len(text1), len(text2)
        dp = [[0] * M for _ in range(L)]
        for i in range(L-1,-1,-1):
            for j in range(M-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1
                    if i+1 < L and j+1 < M:
                        dp[i][j] += dp[i+1][j+1]
                else:
                    a = b = 0
                    if i+1 < L:
                        a = dp[i+1][j]
                    if j+1 < M:
                        b = dp[i][j+1]
                    dp[i][j] = max(a, b)
        return dp[0][0]

    def longestCommonSubsequence_Recursive(self, text1: str, text2: str) -> int:
        """
        Recursive Solution with memoization.
        """
        self.L = len(text1)
        self.M = len(text2)
        self.s1 = text1
        self.s2 = text2
        self.memo = [[None] * self.M for _ in range(self.L)]
        print(self.memo)
        return self.lcs(0, 0)
    def lcs(self, i, j):
        if i >= self.L or j >= self.M:
            return 0
        else:
            if self.memo[i][j] is None:
                if self.s1[i] == self.s2[j]:
                    self.memo[i][j] = 1 + self.lcs(i+1, j+1)
                else:
                    self.memo[i][j] = max(self.lcs(i+1,j), self.lcs(i,j+1))
            return self.memo[i][j]
