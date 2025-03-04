"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]):
        # For memoization
        self._map_ = {}
        # To store output across multiple invocations
        self.out = []
        self._wordBreak(s, wordDict)
        return self.out
    def _wordBreak(self, s: str, wordDict: List[str], prefix=''):
        """
        Algo: For any 'index' if s[0]...s[index-1] is a word then :
        1. Select this word and continue to find more words in s[index]....s[N-1]
        2. Reject this word and continue to find words. This is needed if there are words
           that share a prefix like "cats" and "cat" OR "sand" and "and"
        """
        if len(s) == 0:
            return prefix
        memo = self._map_.get(s, None)
        if memo is not None:
            return memo
        for index in range(1,len(s)+1):
            words = []
            if s[:index] in wordDict:
                ret = self._wordBreak(s[index:], wordDict, prefix=" ".join([prefix, s[:index]]).strip())
                if ret is not None:
                    self._map_[s[index:]] = ret
                    words.append(self._map_[s[index:]])
                    self.out.extend(words)
        return None
