"""
Palindrome Partitioning II
Solved
Hard
Topics
conpanies icon
Companies
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters only.
"""
"""
Approach:
DP Optimal SubStructure: find the 'k' between i and j s.t that i..k and k+1...j is partioned optimally. i..j is just 1 + that value.
Optimizations: Need a quick way to know if i...j is a palindorm, maintain a 2D pre-computed matrix for that.
"""

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False]*n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(n-1):
            is_palindrome[i][i+1] = (s[i] == s[i+1])
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i+length-1
                is_palindrome[i][j] = (s[i] == s[j]) and is_palindrome[i+1][j-1]
        
        dp = [0]*n
        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = min(dp[j] + 1 for j in range(i) if is_palindrome[j+1][i])
        return dp[-1]
