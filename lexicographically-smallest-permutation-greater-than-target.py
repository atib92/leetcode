"""
Lexicographically Smallest Permutation Greater Than Target
Solved
Medium
Topics
conpanies icon
Companies
Hint
You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

 

Example 1:

Input: s = "abc", target = "bba"

Output: "bca"

Explanation:

The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
The lexicographically smallest permutation that is strictly greater than target is "bca".
Example 2:

Input: s = "leet", target = "code"

Output: "eelt"

Explanation:

The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
The lexicographically smallest permutation that is strictly greater than target is "eelt".
Example 3:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
None of them is lexicographically strictly greater than target. Therefore, the answer is "".
 

Constraints:

1 <= s.length == target.length <= 300
s and target consist of only lowercase English letters.
"""
class Solution:
    """
    We solve this recursively similar to how we compute all permuations of a string.
    1. Sort the string
    2. Try to find next permuation that is strictly greater than the target string
    3. During pivot selection, if we find letter at s  > letter at t -> we have found the ans
    4. If letter at s < letter at t, this cannot be the pivot and we need to check further
    5. if letter at s == letter at t, this can be the pivot if we can find a s < t in the remaining s and t
    """
    def lgp(self, s, target):
        n = len(s)
        pivot = 0
        last_pivot = None
        while(pivot < n):
            if s[pivot] == last_pivot:
                pivot += 1
                continue
            else:
                last_pivot = s[pivot]
            if s[pivot] < target[0]:
                pivot += 1
            elif s[pivot] > target[0]:
                return s[pivot] + ''.join(s[:pivot] + s[pivot+1:])
            else:
                ret = self.lgp(''.join(s[:pivot] + s[pivot+1:]), target[1:])
                if ret is not None:
                    return s[pivot] + ret
                else:
                    pivot += 1
        return None
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        s, target = ''.join(sorted(s)), target
        ret =  self.lgp(s,target)
        if not ret:
            return ""
        else:
            return ret
