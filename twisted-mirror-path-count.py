"""
Twisted Mirror Path Count
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given an m x n binary grid grid where:

grid[i][j] == 0 represents an empty cell, and
grid[i][j] == 1 represents a mirror.
A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). It can move only right or down. If the robot attempts to move into a mirror cell, it is reflected before entering that cell:

If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.
If this reflection would cause the robot to move outside the grid boundaries, the path is considered invalid and should not be counted.

Return the number of unique valid paths from (0, 0) to (m - 1, n - 1).

Since the answer may be very large, return it modulo 109 + 7.

Note: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.
"""
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        """
        Right : 0 
        Down : 1
        waysRight[r][c]: # of ways to reach cell (r,c) from left (i,e right direction)
        waysDown[r][c]: # of ways to reach call (r,c) from above (i,e down direction)
        """
        R, C = len(grid), len(grid[0])
        waysRight, waysDown = [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]
        # Process first row and col
        waysRight[0][0] = 1
        waysDown[0][0] = 1
        for c in range(C):
            waysRight[0][c] = 1
            if grid[0][c] == 1:
                break # Cannot go further right
        for r in range(R):
            waysDown[r][0] = 1
            if grid[r][0] == 1:
                break # Cannot go further down
        for r in range(1, R):
            for c in range(1, C):
                # waysRight[r][c]
                if grid[r][c-1] == 0:
                    waysRight[r][c] = waysRight[r][c-1] + waysDown[r][c-1]
                else:
                    waysRight[r][c] = waysDown[r][c-1]
                # waysDown[r][c]
                if grid[r-1][c] == 0:
                    waysDown[r][c] = waysDown[r-1][c] + waysRight[r-1][c]
                else:
                    waysDown[r][c] = waysRight[r-1][c]
        return (waysRight[-1][-1] + waysDown[-1][-1]) % 1000000007
