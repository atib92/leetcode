"""
Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If no such uncommon subsequence exists, return -1.
An uncommon subsequence between two strings is a string that is a subsequence of exactly one of them.
"""
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        """
        Brute Force : Find all subsequence of a and b, and for each subsequence in set(a X b)
                      find the longest one that belong to one but not in the other
                      Time: O(2^(n+m))

        Optimal solution: If the strings are identical, there is no uncommon subsequence
                          if they are not, the longest string is safely the longest uncommon subsequence
                          Time: O(n+m)
        """
        return -1 if a == b else max(len(a), len(b))
