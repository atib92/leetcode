"""

Search Pattern (KMP-Algorithm)
Given two strings, one is a text string txt and the other is a pattern string pat. The task is to print the indexes of all the occurrences of the pattern string in the text string. Use 0-based indexing while returning the indices. 
Note: Return an empty list in case of no occurrences of pattern.
"""
class Solution:
    def _create_lps(self, s):
        i = 1
        l = 0
        n = len(s)
        lps = [0] * n
        while(i < n):
            if s[i] == s[l]:
                lps[i] = lps[i-1] + 1
                i += 1
                l += 1
            else:
                if l == 0:
                    lps[i] = 0
                    i += 1
                else:
                    l = lps[l-1]
        return lps
                
    def search(self, pat, txt):
        # code here
        lps = self._create_lps(pat)
        ret = []
        n,m = len(txt), len(pat)
        i = 0
        j = 0
        while(i < n):
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == m:
                    ret.append(i-m)
                    j = lps[j-1]
            else:
                if j > 0:
                    j = lps[j-1]
                else:
                    i += 1
        return ret
