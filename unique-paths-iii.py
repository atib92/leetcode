"""
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:


Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
"""


class Solution:
    """
    Vanially DFS Backtracking with the addtion of nonobstacles count.
    We follow DFS since it allows us to mark and track visited cells naturally as opposed to BFS.
    Note: Caching on @cache dfs (...) won't work since the result of the dfs not only depends on
    the r,c, obstacles. It also depends on the state of the grid caching which is non trivial.
    """
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(r, c, nonobstacles):
            ret = 0
            if r==d_row and c==d_col:
                if nonobstacles == 0:
                    ret = 1
            elif grid[r][c] == 0 or grid[r][c] == 1:
                save = grid[r][c]
                grid[r][c] = -2 # mark visited (undo when backtracking)
                nonobstacles -= 1
                for d_r, d_c in directions:
                    rr, cc = r+d_r, c+d_c
                    if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] != -2 and grid[rr][cc] != -1:
                        x = dfs(rr, cc, nonobstacles)
                        ret += x
                grid[r][c] = save
                nonobstacles += 1
            return ret
        R, C = len(grid), len(grid[0])
        nonobstacles = 0
        directions = [(0,+1), (0,-1), (-1,0),(+1,0)]
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    s_row, s_col = r, c
                    nonobstacles += 1
                elif grid[r][c] == 2:
                    d_row, d_col = r, c
                elif grid[r][c] == 0:
                    nonobstacles += 1
                elif grid[r][c] == -1:
                    continue
        return dfs(s_row, s_col, nonobstacles)
