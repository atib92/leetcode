"""
Repeated DNA Sequences
Attempted
Medium
Topics
conpanies icon
Companies
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        out = set()
        n = len(s)
        for i in range(n-10+1):
            if s[i:i+10] not in out: # Extra optimization to not recheck substrings which have already been seen twice.
                if s[i:i+10] in seen:
                    out.add(s[i:i+10])
                else: # Adding to set is NOP but we do it anyways to optimise runtime. Maybe python would use a hash to already make seen.add O(1) but we do not take any chances.
                    seen.add(s[i:i+10])
        return list(out)
