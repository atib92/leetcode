""" 
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
* Insert a character
* Delete a character
* Replace a character
"""
class Solution:
    """ 
    Algorithm: Given word1[i], word2[j]. At every step there are 3 operations we can perform:
    1. Update (+1 Operation) word1[i] and make it same as word2[j] and recursively convert word1[i+1:] to  word2[j+1:]
    2. Delete (+1 Operation) word1[i] and recursively convert word1[i+1:] to  word2[j:]
    3. Add (+1 Operation) word2[j] at word1[i] and recursively convert word1[i:] to  word2[j+1:]
    """
    def minDistance(self, word1: str, word2: str) -> int:
        self.L1, self.L2 = len(word1), len(word2)
        if self.L1 == 0:
            return self.L2
        if self.L2 == 0:
            return self.L1
        self._dp_ = [[None] * self.L2 for _ in range(self.L1)]
        self._dp_[0][0] = self._minDistance(word1, word2, 0, 0)
        return self._dp_[0][0]
    def _minDistance(self, word1: str, word2: str, i, j) -> int:
        if i < self.L1 and j < self.L2 and self._dp_[i][j] is not None:
            return self._dp_[i][j]
        if (i >= self.L1 and j >= self.L2):
            return 0
        elif i >= self.L1:
            return self.L2-j
        elif j >= self.L2:
            return self.L1-i
        else:
            if word1[i] == word2[j]:
                self._dp_[i][j] =  min(
                    1 + self._minDistance(word1, word2, i+1, j),
                    self._minDistance(word1, word2, i+1, j+1),
                    1 + self._minDistance(word1, word2, i, j+1)
                )
            else:
                self._dp_[i][j] =  min(
                    1 + self._minDistance(word1, word2, i+1, j),
                    1 + self._minDistance(word1, word2, i+1, j+1),
                    1 + self._minDistance(word1, word2, i, j+1)
                )
            return self._dp_[i][j]
