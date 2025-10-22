"""
Making A Large Island
Solved
Hard
Topics
conpanies icon
Companies
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""
class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.largest = 1
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            return self.find(self.parents[x])
    def union(self, x, y):
        xrep, yrep = self.find(x), self.find(y)
        if xrep != yrep:
            if self.sizes[xrep] >= self.sizes[yrep]:
                self.parents[yrep] = xrep
                self.sizes[xrep] += self.sizes[yrep]
                self.largest = max(self.largest, self.sizes[xrep])
            else:
                self.parents[xrep] = yrep
                self.sizes[yrep] += self.sizes[xrep]
                self.largest = max(self.largest, self.sizes[yrep])
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        1. Do DSU for the orignial grid and calculate the no. of componenets and sizes
        2. For every 0, try to do Union with neighboring 1s and see whats the biggest component we can get
        """
        R, C = len(grid), len(grid[0])
        dsu = DSU(R*C)
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    for dr,dc in [(0,-1), (0,+1), (-1,0), (+1,0)]:
                        if 0 <= r+dr < R and 0 <= c+dc < C and grid[r+dr][c+dc] == 1:
                            dsu.union(r*C+c, (r+dr)*C+(c+dc))
        largest_island = dsu.largest
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    unique_parents = set([])
                    cum_size = 0
                    for dr,dc in [(0,-1), (0,+1), (-1,0), (+1,0)]:
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == 1:
                            parent = dsu.find(rr*C + cc)
                            if parent not in unique_parents:
                                unique_parents.add(parent)
                                cum_size += dsu.sizes[parent]
                    largest_island = max(largest_island, cum_size+1)
        return largest_island
