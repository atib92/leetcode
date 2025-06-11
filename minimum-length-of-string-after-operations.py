"""
 Minimum Length of String After Operations
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s.

You can perform the following process on s any number of times:

Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
Delete the closest occurrence of s[i] located to the left of i.
Delete the closest occurrence of s[i] located to the right of i.
Return the minimum length of the final string s that you can achieve.

 

Example 1:

Input: s = "abaacbcbb"

Output: 5

Explanation:
We do the following operations:

Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".
Example 2:

Input: s = "aa"

Output: 2

Explanation:
We cannot perform any operations, so we return the length of the original string.

 

Constraints:

1 <= s.length <= 2 * 105
s consists only of lowercase English letters.
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        """
        1. Order doesn't matter.
        eg. "abaacbcbb"
        {a:3,b:4,c:2} +1 +2
        1 b -> b
        2 bb -> bb
        3 bbb -> b
        4 bbbb -> bb
        5 bbbbb -> b
        6 bbbbbb -> bb
        so: odd +1 even +2
        """
        out = 0
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for ch, val in freq.items():
            if val % 2 == 0:
                # even count
                out += 2
            else:
                out += 1
        return out
"""
Future Improvements: Since chars can only be lower case alphabes, the freq. counting can be done using array[] of size 26 where charecter ch's frequence is in array[ord(ch)-ord('a')]
"""
