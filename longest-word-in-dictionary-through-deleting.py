"""
Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

 

Example 1:

Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
Example 2:

Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"
 

Constraints:

1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s and dictionary[i] consist of lowercase English letters.
"""
class Solution:
    def _match(self, s, word):
        L, M = len(s), len(word)
        i, j = 0, 0
        while(i<L and j<M):
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == M:
            return True
        else:
            return False
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        """
        Iterate over the dict words and match(s, word). Save the latest best match.
        Best Match : Longest match. Resolve conflict by chooing the lexicographically smaller one.
        """
        longest_match = ""
        for index, word in enumerate(dictionary):
            match = self._match(s, word)
            if match is True:
                if len(word) > len(longest_match):
                    longest_match = word
                elif len(word) == len(longest_match):
                    longest_match = min(word, longest_match)
        return longest_match
