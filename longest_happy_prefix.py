"""
Source: https://leetcode.com/problems/longest-happy-prefix/description/
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

 

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
Example 2:

Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.

"""
class Solution:
    """
    This is nothing but the PI (Longest Prefix which is also a Suffix a.k.a lps) matrix computation step of the KNP string matching algo.
    We will create the LPS array when LPS[i] denotes the longest proper prefix of s[:i] that is also a suffix. The answer is nothing but
    LPS[-1] i,e the longest proper prefix of S that is also a suffix.
    """
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
        i = 1
        l = 0
        while(i < n):
            if s[i] == s[l]:
                lps[i] = l + 1
                l += 1
                i += 1
            else:
                if l == 0:
                    lps[i] = 0
                    i += 1
                else:
                    l = lps[l-1]
        return s[:lps[-1]]
