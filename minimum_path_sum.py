""" 
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

from copy import deepcopy
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        INF = 100000
        R, C = len(grid), len(grid[0])
        path = deepcopy(grid)
        for r in range(R):
            for c in range(C):
                if r == 0 and c==0:
                    continue
                from_top = from_left = 100000
                if r > 0:
                    from_top = path[r-1][c]
                if c > 0:
                    from_left = path[r][c-1]
                path[r][c] += min(from_top, from_left)
        return path[R-1][C-1]
