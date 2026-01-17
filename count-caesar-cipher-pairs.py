'''
Count Caesar Cipher Pairs
Solved
Medium
Topics
Hint
You are given an array words of n strings. Each string has length m and contains only lowercase English letters.

Two strings s and t are similar if we can apply the following operation any number of times (possibly zero times) so that s and t become equal.

Choose either s or t.
Replace every letter in the chosen string with the next letter in the alphabet cyclically. The next letter after 'z' is 'a'.
Count the number of pairs of indices (i, j) such that:

i < j
words[i] and words[j] are similar.
Return an integer denoting the number of such pairs.

 

Example 1:

Input: words = ["fusion","layout"]

Output: 1

Explanation:

words[0] = "fusion" and words[1] = "layout" are similar because we can apply the operation to "fusion" 6 times. The string "fusion" changes as follows.

"fusion"
"gvtjpo"
"hwukqp"
"ixvlrq"
"jywmsr"
"kzxnts"
"layout"
Example 2:

Input: words = ["ab","aa","za","aa"]

Output: 2

Explanation:

words[0] = "ab" and words[2] = "za" are similar. words[1] = "aa" and words[3] = "aa" are similar.

 

Constraints:

1 <= n == words.length <= 105
1 <= m == words[i].length <= 105
1 <= n * m <= 105
words[i] consists only of lowercase English letters.
'''

class Solution:
    def countPairs(self, words: List[str]) -> int:
        '''
        Reduce each word to its canonical form. Once we know the unique canonical forms and the number of
        words which have the same form say N, then pairs contributed by these words are N*(N-1)/2
        '''
        @cache
        def wordhash(word):
            '''
            Reduces the word to its canonical form. The canonical form is derived by using the first letter
            as the pivot and finding the relative distance of each letter from the pivot.
            '''
            _hash = []
            base = ord(word[0])
            for ch in word[1:]:
                _hash.append(str((ord(ch)-base)%26))
            return '.'.join(_hash)
        d = {}
        for word in words:
            _wordhash = wordhash(word)
            d[_wordhash] = d.get(_wordhash, 0) + 1
        #print(d)
        count = 0
        for wh, val in d.items():
            count += (val * (val - 1)) // 2
        return count
