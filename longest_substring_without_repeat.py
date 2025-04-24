"""
Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    """
    We employ a typical sliding window algorithm here.
    1. As long as the leading pointer adds a new element, we add the elem.
    2. The moment the leading pointer adds a repeat element, we shrink the window
       so that we can add the leading pointer element.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            L, R, _max, N = 0, 0, 0, len(s)
            elems = set()
            while(L <= R and L < N and R < N):
                if s[R] not in elems:
                    elems.add(s[R])
                    _max = max(_max, R-L+1)
                    R += 1
                else:
                    while(s[R] in elems):
                        elems.remove(s[L])
                        L += 1
            return _max
