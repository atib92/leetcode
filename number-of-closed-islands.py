"""
Number of Closed Islands
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""
from collections import deque

class Solution:
    """
    Standard BFS Flood Fill with closed island detection. Basically an island is closed if any land in the island
    is not surrouned by a water on all sides. This only happens if any land is an edge cell.
    """
    def closedIsland(self, grid: List[List[int]]) -> int:
        def traverseIsland(row, col) -> int:
            q = deque()
            grid[row][col] = -1 # Mark
            q.append((row, col))
            ret = True
            while(q):
                row, col = q.popleft()
                if row == 0 or row == R-1 or col == 0 or col == C-1:
                    ret = False # Edge cell in the island. Not closed
                for dr, dc in [(0,-1), (0,+1), (-1,0), (+1,0)]:
                    if 0 <= row + dr < R and 0 <= col + dc < C and grid[row+dr][col+dc] == 0:
                        grid[row+dr][col+dc] = -1
                        q.append((row+dr, col+dc))
            return ret
        R, C = len(grid), len(grid[0])
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    count += int(traverseIsland(r, c))
        return count
