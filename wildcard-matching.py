"""
Wildcard Matching
Solved
Hard
Topics
conpanies icon
Companies
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
"""


"""
Intuition : Dynamic Programming 
The problem has the Optimal Substructure Property that allows you solve it via DP.

Approach
Optimal Substructure: Let's define the dp state as dp(i,j) which is True if p[:i] matches s[:j] and else otherwise.

We can compute the state dp(i,j) if we know the match result of the following previous states:

dp(i-1, j-1)
dp(i-1, j)
dp(i, j-1)
Details:
dp(i,j) : p[0,i) matches s(0,j] only if:

Shorter pattern p[0,i-1) matched string s(0,j] and the current pattern char is a '*'
Same pattern p[0,i) matched the shorter string s(0,j-1] and the current pattern char is a '*'
Shorter pattern p[0,i-1) matched matched the shorter string s(0,j-1] and the current pattern char matches the current string charecter which is when both chars are same or pattern charn is a wildcard
Complexity
Time complexity:
O(N*M)
Space complexity:
O(N*M)
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N, M = len(p), len(s)
        dp = [[False] * (M+1) for _ in range(N+1)]
        dp[0][0] = True
        for i in range(1, N+1):
            if p[i-1] == '*':
                dp[i][0] = dp[i-1][0] == True
        for i in range(1, N+1):
            for j in range(1, M+1):
                if dp[i-1][j-1] == True:
                    if p[i-1] == s[j-1] or p[i-1] == '?' or p[i-1] == "*":
                        dp[i][j] = True
                        continue
                if dp[i][j-1] == True or dp[i-1][j] == True:
                    if p[i-1] == "*":
                        dp[i][j] = True
                        continue
        return dp[N][M]


"""
Just out of curiosity, there is also a suboptimal Recursive solution (with caching)
"""
class Solution:
    def isMatch_Recursion(self, s: str, p: str) -> bool:
        @cache
        def _is_match(s_index, p_index):
            if s_index == len_s and p_index == len_p:
                return True
            elif s_index < len_s and p_index < len_p:
                ret = False
                if p[p_index] == "*":
                    for j in range(s_index, len_s+1):
                        sub_match = _is_match(j ,p_index+1)
                        if sub_match == True:
                            return True
                        else:
                            continue
                    return False
                elif p[p_index] == "?":
                    return _is_match(s_index+1, p_index+1)
                else:
                    if s[s_index] == p[p_index]:
                        return _is_match(s_index+1, p_index+1)
                    else:
                        return False
            else:
                #return s == ""
                if p_index < len_p:
                    return all(x == '*' for x in p[p_index:])
                return s_index == len_s and p_index == len_p
        len_s, len_p = len(s), len(p)
        return _is_match(0,0)

"""
For comaparision, the Bottom Up DP approach ran in ~350ms while the Top Down recursive solution took ~1200ms (for all leetcode test cases ~ 1000)
"""
