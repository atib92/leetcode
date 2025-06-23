"""
Permutation in String
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
from copy import deepcopy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        1. Obviously we will match s1 and a substring of s2 using a char counter
        2. if the new element is not in the target i,e our pending_counter dict, we will start a fresh window from the next element
        3. If the new element is in the target i,e in the pending_counter dict, we can continue the current window.

        Note: There is an interesting nuance where the new element is not in pending counter but in freq_counter i,e we have already
              added that element in the substring. The best thing at this point in time would be to shrink the window till the point
              the last time when this element was seen in s2 and once more to flush out the last occurance.
        """
        freq_counter = {}
        for ch in s1:
            freq_counter[ch] = freq_counter.get(ch, 0) + 1
        l = 0
        r = 0
        n = len(s2)
        pending_counter = deepcopy(freq_counter)
        while(r < n):
            #print(f'window {l}-{r} substring {s2[l:r+1]} pending_counter {pending_counter} freq_counter {freq_counter}')
            if s2[r] in pending_counter:
                pending_counter[s2[r]] -= 1
                if pending_counter[s2[r]] == 0:
                    del pending_counter[s2[r]]
                if not pending_counter:
                    return True
                r += 1
            elif s2[r] not in freq_counter:
                # This elem is not in the target so the next window has to start fresh from next elem
                r += 1
                l = r
                pending_counter = deepcopy(freq_counter)
            else:
                # This elem is not in pending_counter but in freq_counter i,e
                # we can potentially restart the window from next to when this
                # elem was found
                while(s2[l] != s2[r]):
                    pending_counter[s2[l]] = pending_counter.get(s2[l], 0) + 1
                    l += 1
                pending_counter[s2[l]] = pending_counter.get(s2[l], 0) + 1
                l += 1
        return False
