"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""
from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        '''
        1. Mark the first island
            Find the first land (1) in the grid and do a BFS from there to mark all lands in that island. 
            Also save the lands in a separate queue for the second BFS later.
        2. Start a multi BFS from each land on the first island and keep a track of distance/levels until
            you touch the second island
        '''
        def traverse_island(row, col):
            queue = deque() # primary queue for this island
            save = deque() # save for later
            queue.append((row, col))
            save.append((row, col))
            grid[row][col] = -1 # Mark
            while(queue):
                r, c = queue.popleft()
                for dr, dc in [(0,-1), (0,+1), (-1,0), (+1,0)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        # connected land in the same island
                        grid[nr][nc] = -1 # Mark
                        queue.append((nr, nc))
                        save.append((nr, nc))
            return save
        def create_bridge(q):
            # Multi BFS from each land in the first island
            d = 0
            while(q):
                d += 1
                l = len(q)
                for _ in range(l):
                    r, c = q.popleft()
                    for dr, dc in [(0,-1), (0,+1), (-1,0), (+1,0)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < R and 0 <= nc < C:
                            if grid[nr][nc] == 0:
                                grid[nr][nc] = -1
                                q.append((nr, nc))
                            elif grid[nr][nc] == 1:
                                # Found the second island
                                return d-1
                            else:
                                # already marked 
                                continue
            return d
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    q = traverse_island(r, c)
                    return create_bridge(q)
        return -1
