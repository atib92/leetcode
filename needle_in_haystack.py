"""
Source: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=problem-list-v2&envId=string-matching
Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
class Solution:
    def _build_lps(self, s:str):
        n = len(s)
        i = 1
        lps = [0] * n
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
        return lps
    def strStr(self, haystack: str, needle: str) -> int:
        """
        We will use the KNP algo to find the first match and exit.
        """
        lps = self._build_lps(needle)
        #print(f'needle {needle} lps {lps}')
        i = j = 0
        n = len(haystack)
        m = len(needle)
        while(i < n):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i-m # In a tradition KNP, you would continue to find more matches by doing j = lps[j-1] before you store the match.
            else:
                if j > 0:
                    j = lps[j-1]
                else:
                    i += 1
        return -1
