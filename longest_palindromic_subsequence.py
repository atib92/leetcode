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


"""
Followup: Count the total number of palindromic subsequences (repeat allowed)
"""
class Solution:
    """
    dp[i][j] is the count of plaindromic subsequences in the closed interval [i,j] in the input string s.
    if s[i] == s[j], the total # is the sum of dp[i+1][j] and dp[i][j-1] and the new palindrom s[i]s[j]
    if s[i] != s[j] we only have dp[i+1][j] and dp[i][j-1] but both the intervals contains dp[i+1][j-1] so we subtract that to not end up double counting
    """
    def countPS(self,s):
        n = len(s)
        dp = [[0]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i + 1 < n:
                dp[i][i+1] = 3 if s[i] == s[i+1] else 2
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                dp[i][j] = dp[i+1][j] + dp[i][j-1]
                if s[i] == s[j]:
                    dp[i][j] += 1
                else:
                    dp[i][j] -= dp[i+1][j-1]
        return dp[0][n-1]
"""
Followup 2: List all the palindromic subsequences (don't just count)
We we save intermediate solutions in a dp array, the amount of storage would explode. A recursive
solution is better in this case
"""
def findPS(self, s: str):
    n = len(s)
    # Memoization table to store the set of palindromic subsequences
    # for a substring s[i..j].
    # Use a dictionary for sparse memoization: memo[(i, j)] -> set of strings
    memo = {}

    def findPS_recursive(i, j):
        # 1. Base Cases
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i > j:
            return set()  # Empty substring
        
        if i == j:
            return {s[i]}  # Single character is a palindrome
        
        # 2. Recursive Step
        
        # Start with the union of the two overlapping subproblems:
        # PSs that don't use s[i] (from s[i+1..j])
        set1 = findPS_recursive(i + 1, j) 
        # PSs that don't use s[j] (from s[i..j-1])
        set2 = findPS_recursive(i, j - 1)
        
        current_ps = set1.union(set2)
        
        if s[i] == s[j]:
            c = s[i]
            
            # Palindromes formed by enclosing PSs from the inner substring s[i+1..j-1]
            inner_ps = findPS_recursive(i + 1, j - 1)
            
            # Add the new palindromes: c..c
            new_ps = set()
            
            # 1. Palindromes of length >= 3: c + p + c, where p is from inner_ps
            for p in inner_ps:
                new_ps.add(c + p + c)
            
            # 2. Palindrome of length 1 (c) and length 2 (cc) 
            # Note: 'c' is already included in inner_ps if i+1 <= j-1, 
            # but to be safe and cover i+1 > j-1 (adjacent chars), we explicitly add 'c' and 'cc'.
            new_ps.add(c) 
            new_ps.add(c + c)
            
            current_ps.update(new_ps)

        # Store result and return
        memo[(i, j)] = current_ps
        return current_ps

    # The final answer is the set of PSs for the entire string s[0..n-1]
    return findPS_recursive(0, n - 1)
