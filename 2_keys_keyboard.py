"""
2 Keys Keyboard
Solved
Medium
Topics
conpanies icon
Companies
Hint
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

 

Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0
 

Constraints:

1 <= n <= 1000
"""
class Solution:
    def minSteps_rememo(self, n: int) -> int:
        """
        Simple Recursion with memoization O(2^N) but works for all test cases with memoization
        paste: screen += clipboard
        """
        steps = float("inf")
        @cache
        def _minStep(s, c):
            if s == n:
                return 0
            elif s > n or c > n:
                return float("inf")
            else:
                if c != s:
                    copy = _minStep(s, s)
                else:
                    copy = float("inf")
                if c > 0:
                    paste = _minStep(s+c, c)
                else:
                    paste = float("inf")
                return 1 + min(copy, paste)
        return _minStep(1, 0)
      
    def minSteps(self, n: int) -> int:
        """
        The key observation is that we can reach a target 'i' from 'j' only if:
        1. j is a factor of i (By copying once and pasting (j-i)//j number of time)
        2. of all the factors of i, choose the one that causes minimum operations (copy + a number of pastes)
        """
        dp = [float("inf")] * (n+1)
        dp[1] = 0
        for i in range(2, n+1):
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + 1 + (i-1) // j) # This is written this way to align with the observation,
                                                               # A much simpler way of writing is dp[i] + (i // j)
        return dp[n]        
