"""
Smallest Palindromic Rearrangement II
Attempted
Hard
Topics
Hint
You are given a palindromic string s and an integer k.

Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.

Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.

 

Example 1:

Input: s = "abba", k = 2

Output: "baab"

Explanation:

The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".
Example 2:

Input: s = "aa", k = 2

Output: ""

Explanation:

There is only one palindromic rearrangement: "aa".
The output is an empty string since k = 2 exceeds the number of possible rearrangements.
Example 3:

Input: s = "bacab", k = 1

Output: "abcba"

Explanation:

The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".
Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
s is guaranteed to be palindromic.
1 <= k <= 106
"""
from collections import Counter
from math import factorial

class Solution:
    @staticmethod
    def multinomial(counts: Counter) -> int:
        """Return number of unique permutations for given multiset of chars."""
        n = sum(counts.values())
        denom = 1
        for c in counts.values():
            denom *= factorial(c)
        return factorial(n) // denom
    def kth_permuatation(self, s: str, k: int) -> str:
        counts = Counter(s)
        total = self.multinomial(counts)
        if k < 0 or k >= total:
            return None
        result = []
        while counts:
            for ch in sorted(counts):  # lexicographic order
                if counts[ch] == 0:
                    continue
                # try this char as pivot
                counts[ch] -= 1
                block_size = self.multinomial(counts)
                if k < block_size:
                    result.append(ch)
                    break
                else:
                    k -= block_size
                    # Going to next block so add back the ch we remove from count earlier.
                    counts[ch] += 1
            else:
                break
        ret = "".join(result)
        return ret
    def smallestPalindrome(self, s: str, k: int) -> str:
        """
        We know the prefix (and pivot if lenght is odd)
        The question boils down to: In the sorted prefix, what is the kth
        permuation. Once we have that sequence, append the odd char (if any)
        and the suffix which is nothing but the revers of the prefix.

        Refer kth_permuation_duplicates.py to understand the algo behing computing the kth permuation of a string (with duplicates)
        """
        n = len(s)
        if n % 2 == 0:
            # Even
            pivot = ''
        else:
            pivot = s[n//2]
        s = sorted(s[:n//2])
        ks = self.kth_permuatation(s, k-1)
        if ks is None:
            return ''
        else:
            return ks + pivot + ks[::-1]
