"""
Source: https://leetcode.com/problems/pacific-atlantic-water-flow/description/
Pacific Atlantic Water Flow
Solved
Medium
Topics
premium lock icon
Companies
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        We will approach it in reverse order:
        1. Mark all edge cells as either depending on its adjacency from the two oceans.
        2. Then from each edge cell, we will do a BFS if the neigbor ht >= the edge cell height
           implying the flow of water (actually the reverse) and if yes, increment the count
           of the neigbor
        Note: Doing it this way, it boils down to a connected component problem (with ofcourse the height constraint)
        """
        R, C = len(heights), len(heights[0])
        pacific = [ [None] * C for _ in range(R) ]
        atlantic = [ [None] * C for _ in range(R) ]
        # Pacific processing (1st row and 1 col)
        q = deque()
        for c in range(C):
            q.append((0,c))
        for r in range(R):
            q.append((r,0))
        while(q):
            r, c = q.popleft()
            if pacific[r][c] is None: # Not already processed
                pacific[r][c] = 1
                directions = [(-1,0),(0,-1),(+1,0),(0,+1)]
                for rr, cc in directions:
                    if 0 <= r+rr < R and 0 <= c+cc < C and heights[r+rr][c+cc] >= heights[r][c]:
                        q.append((r+rr, c+cc))
        # Atlantic processing (Identical to Pacific Processing: Can be put into a common utility)
        for c in range(C):
            q.append((R-1,c))
        for r in range(R):
            q.append((r,C-1))
        while(q):
            r, c = q.popleft()
            if atlantic[r][c] is None: # Not already processed
                atlantic[r][c] = 1
                directions = [(-1,0),(0,-1),(+1,0),(0,+1)]
                for rr, cc in directions:
                    if 0 <= r+rr < R and 0 <= c+cc < C and heights[r+rr][c+cc] >= heights[r][c]:
                        q.append((r+rr, c+cc))
        if len(q) != 0:
            print(f'q still has elements {len(q)}')
        output = []
        for r in range(R):
            for c in range(C):
                if pacific[r][c] == 1 and atlantic[r][c] == 1:
                    output.append([r,c])
        return output
        
        
        
