""" 
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
"""

class Solution:
    """
    The approach is similar to unique_paths.py except that we added the constraint that there can be obstacles.
    1. A cell is reachable from top/left only if there is no obstacle at the cell location.
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0 # Can't even start
        else:
            R, C = len(obstacleGrid), len(obstacleGrid[0])
            pathGrid = [[0] * C for _ in range(R)]
            pathGrid[0][0] = 1 # We know we can start if we are here
            for r in range(R):
                for c in range(C):
                    if r==0 and c==0:
                        continue
                    else:
                        path, from_above, from_left = 0, False, False
                        if obstacleGrid[r][c] != 1:
                            if r > 0 and pathGrid[r-1][c] > 0:
                                path += pathGrid[r-1][c]
                            if c > 0 and pathGrid[r][c-1] > 0:
                                path += pathGrid[r][c-1]
                        pathGrid[r][c] = path
            return pathGrid[R-1][C-1]
