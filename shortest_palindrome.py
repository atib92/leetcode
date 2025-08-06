"""
Shortest Palindrome
Solved
Hard
Topics
conpanies icon
Companies
You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
"""
class Solution:
    def shortestPalindrome_ExpandPivot_SubOptimal(self, s: str) -> str:
        """
        This is O(N^2) : 121/126 test cases passed.
        Idea: We compute a dp matrix s.t dp[i][j] tells us if s[i,j] is a palindrome. We
        use the above dp matrix to start from a 'pivot' point and expand a window to see
        if can cover all charecters till index 0 in a palindromic substring. If yes,
        whatever is left from the right is what needs to be appended (in reverse) to the
        front for the final string to become a palindrome.
        O(N^2)
        """
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = True
            if i+1 < N:
                dp[i][i+1] = (s[i] == s[i+1])
        for l in range(3, N+1):
            for i in range(N-l+1):
                j = i + l - 1
                if s[i] == s[j] and dp[i+1][j-1] == True:
                    dp[i][j] = True
        j = N-1
        while(j > 0 and dp[0][j] == False):
            j -= 1
        return s[j+1:][::-1] + s
    def shortestPalindrome(self, s: str) -> str:
        """
        Use LPS: LPS stands from the Longest Prefix which is also a Suffix from
        the KMP pattern matching algorithm.

        Think of the String as |<---X--->|--Y--| where X is the palindromic part and Y isn't.
        If we reverse the string, it becomes:
        |<---X--->|--Y-->|<--Y--||<---X--->|
        Now if you see, X is the LPS of the appended string. We can get LPS[-1], that is the index
        from which if we starting appending chars in the front, we will make s a palindrome.

        Note: The '#' is just so that we donot have to write special checks when input is an empty string.
        Time : O(N) We only iterate once over the (double) string
        Space : O(N) Space for the LPS array
        """
        n = len(s)
        s_bar = s + '#' + s[::-1]
        n_bar = len(s_bar)
        lps = [0] * (n_bar)
        l = 0 # Last lps
        i = 1 # lps of first index is always 0. We consider proper prefixes
        while(i < n_bar):
            if s_bar[i] == s_bar[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l == 0:
                    lps[i] = 0
                    i += 1
                else:
                    l = lps[l-1]
        k = lps[n_bar-1]
        return s[k:][::-1] + s 
