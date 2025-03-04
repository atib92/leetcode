"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""
from collections import deque

class Solution:
    """
    Algo: Brute force is to do BFS from all nodes and whenever you rot an orange, update the "rot time" if its smaller than the prev (in the prev BFS iteration) rotting time.
          However this approach is super costly. We can do much better with a MULTI-BFS approach as follows:
          Pre-Processing : Find all rotten oranges and enque them all. 'time' is set to zero since these oranges are rotten from start.
          Multi BFS : Unlike the vaniall BFS where we dequeu just one node and enqueu all its connected nodes, here we deque all nodes and enque the super set of all connected
          nodes. The idea it deque all oranges that got rotten at the prev time interval and enque all that are getting rotten at the current time interval. Since BFS by nature
          is level by level, we are sure that no orange that had got rotten at an earlier time can get rotten at a better time.
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        Q = deque()
        time = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    Q.append((row, col)) # row, col, time
                    print(f"Enque ({row},{col})")
                elif grid[row][col] == 1:
                    fresh_oranges += 1
        while(len(Q) > 0 and fresh_oranges > 0):
            time += 1
            popped_oranges = []
            while(len(Q) > 0):
                popped_oranges.append(Q.popleft())
            for popped in popped_oranges:
                row, col = popped[0], popped[1]
                #print(f'Deque ({row},{col})')
                directions = [[0,-1],[0,+1],[-1,0],[+1,0]]
                for r,c in directions:
                    new_row, new_col = row + r, col + c
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                        fresh_oranges -= 1
                        grid[new_row][new_col] = 2
                        Q.append((new_row, new_col))
        if fresh_oranges == 0:
            return time
        else:
            return -1
