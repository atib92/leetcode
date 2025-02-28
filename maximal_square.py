"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""
from copy import deepcopy
class Solution:
    """
    The idea is to incrementally try to find bigger and bigger squares by linearly traversing the matrix.
    dp[i][j] stores the maximal square that ends at this cell and we greedily increment it by 1 on top of
    the smallest square thats ends on the three neighboring cells.
    """
    def _get(self, row, col, matrix):
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            return int(matrix[row][col])
        else:
            return 0
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = deepcopy(matrix)
        _max = 0
        for row in range(R):
            for col in range(C):
                if matrix[row][col] == '1':
                    from_above = self._get(row-1, col, dp) 
                    from_left = self._get(row, col-1, dp)
                    from_diag = self._get(row-1, col-1, dp)
                    dp[row][col] = min(from_above, from_left, from_diag) + 1
                    _max = max(_max, dp[row][col])
        return _max ** 2
