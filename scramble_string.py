"""
Scramble String
Solved
Hard
Topics
conpanies icon
Companies
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

 

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
Example 3:

Input: s1 = "a", s2 = "a"
Output: true
 

Constraints:

s1.length == s2.length
1 <= s1.length <= 30
s1 and s2 consist of lowercase English letters.
"""
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        dp = [[[False] * (n+1) for _ in range(n)] for _ in range(n)]
        # for l=1, two strings are only scrambled version of each other if they are identical !
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]
        # For every > 1 lenghth 'l' substring starting from index i in s1 and index j in s2
        for l in range(2, n+1):
            for i in range(n-l+1):
                for j in range(n-l+1):
                    """
                    if any k exists in [1,l) s.t it cuts s1 and s2 into two segments
                    which are scramble'able
                    Case1: 
                    s1: i....*........i+l
                         < k >
                    s2: j....*........j+l
                    first segment s1[i:i+k] matches with first segment s2[j:j+k] i,e dp[i][j][k] == True
                    and
                    2nd segment s1[i+k:l] matches with second segment s2[j+k:j+l] i,e dp[i+k][j+k][l-k] == True

                    Case2
                    s1: i....*........i+l
                         < k >
                    s2: j.......*.....j+l
                                 < k >
                    dp[i][j+l-k][k] == True and dp[i+k][j][l-k]
                    """
                    for k in range(1, l):
                        if (dp[i][j][k] and dp[i+k][j+k][l-k]) or (dp[i][j+l-k][k] and dp[i+k][j][l-k]):
                            dp[i][j][l] = True
                            break
        return dp[0][0][n]
