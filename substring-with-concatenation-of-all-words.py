"""
Substring with Concatenation of All Words
Solved
Hard
Topics
premium lock icon
Companies
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""
class Solution:
    def print(self, s:str):
        #print(s)
        pass
    def _find_starting_indices(self, substring:str, M:int, N:int) -> List[int]:
        """
        substing is of length MN and should have be a permuation of the N words of each length M
        pontential_words starts from 0, M, 2M, (N-1)M...
        Example: 
        substring = barfoo
        words = [foo, bar] M=3, N=2
        """
        substring_map = {}
        for word_index in range(N):
            potential_word = substring[word_index*M:(word_index+1)*M]
            substring_map[potential_word] = 1 + substring_map.get(potential_word, 0)
        self.print(f'substring {substring} map {substring_map}')
        for key, val in substring_map.items():
            if self.words_map.get(key, 0) != val:
                return False
        return True

        
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        1. Create a words frequency counter
        2. Iterate over the input string's substring (of size = size of any concatenated string)
        3. Check if the freq counter of 1 and 2 matches.
        Time: O(len(s) * len(words))
        
        """
        N = len(words)
        M = len(words[0])   # Safe since 1 <= words.length <= 5000
        LCS = M*N           # Length of any concatenated string
        LS = len(s)         # Lenght of the input string
        self.words_map = {} # Since words could repeat, we can't just have a set. We need to consider the count !
        for word in words:
            self.words_map[word] = self.words_map.get(word, 0) + 1
        self.print(f'words_map {self.words_map}')
        out = []
        for start in range(0,LS):
            # substring is a candiate concatinated string
            substring = s[start:start+LCS]
            self.print(f'substring {substring}')
            if len(substring) < LCS:
                break
            if self._find_starting_indices(substring, M, N):
                out.append(start)
            start += M
        return out
            
