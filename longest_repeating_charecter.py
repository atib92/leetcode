'''
424. Longest Repeating Character Replacement
Solved
Medium
Topics
conpanies icon
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''

class Solution:
    def characterReplacement_v1(self, s: str, k: int) -> int:
        '''
        APPROACH 1: We basically use every letter as the pivot and for every pivot we find out
                    what is the longest homogenous substring we can make. We end up doing this
                    26 times !!
        '''
        def characterReplacementHelper(target):
            '''
                Find the longest substring of the target letter by
                converting max k letters
            '''
            l = 0
            count = 0 # count of non target letters, shd not exceed k
            ans = 0
            for r, letter in enumerate(s):
                # window ending at r
                if letter != target:
                    count += 1
                while count > k:
                    # more than rquired edits are required -> slide l forward
                    if s[l] != target:
                        count -= 1
                    l += 1
                # guranteed that window ends at r and <= k non target letter -> valid window
                ans = max(ans, r-l+1)
            return ans
        ans = 0
        for offset in range(26):
            target = chr(ord('A') + offset)
            ans = max(ans, characterReplacementHelper(target))
        return ans
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        APPROACH 2: This is marginally hard and relies on the assumption that
                    in any substring / window, the most frequent letter can be
                    used as the pivot to convert that window to a homogenous
                    substring. This way we only need a single pass
                    Mental Nudge: If you are having difficultly understanding the correctness of this assumption,
                    think of it this way: In any window if there a non max frequent letter that can be used as a
                    pivot to convert the window to a homegenous winow with <= k edits, the max frequent letter can
                    be definitely used as the pivot to form a homogenous window ( with less edits than required by
                    the non max freq element)
        '''
        freq = {}
        l = 0
        max_freq = 0
        ans = 0
        for r, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            # highest frequency char
            max_freq = max(max_freq, freq[ch])
            # replacements needed > k
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans




