"""
Number of Islands II
Solved
Hard
Topics
conpanies icon
Companies
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:


Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
Example 2:

Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]
 

Constraints:

1 <= m, n, positions.length <= 104
1 <= m * n <= 104
positions[i].length == 2
0 <= ri < m
0 <= ci < n
"""
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """
        Brute Force:
        Maintain a m*n grid. Everytime a 1 is added, do a BFS from all 1's and count the number of
        islands. Keep a visited marker to avoid processing the same cell more than once. The number
        of islands at any point in time is the number of BFS run.
        Time: O(L*N^2)

        Union Find:
        Think of cells as vertices. Assign each cell a unique identity, eg. 
        0,0 - 0
        0,1 - 1
        0,2 - 2
        1,0 - 3....
        r,c - r*C + c where r goes from 0 to R-1 call it vertex: 'rc'
        1. When a cell is converted to 1: it means vertex vertex 'rc' is added to the graph.
        2. Check if any neighbor of vertex 'rc' is also 1. If yes, perform union find.
        3. The number of distinct connected components after a land addition is the num of islands

        Furher optimization: We can keep a hash of vertices and index in islands for O(1) find.
        """
        def get_vertex(r,c):
            return r*n + c
        def add_vertex(v):
            islands.append({v})
        def find_vertex(v):
            for index, island in enumerate(islands):
                if v in island:
                    return index
        def union_vertices(index1, index2):
            islands[index1] = set.union(islands[index1], islands[index2])
            islands.pop(index2)
        def union_find(v1, v2):
            index1 = find_vertex(v1)
            index2 = find_vertex(v2)
            if index1 != index2:
                union_vertices(index1, index2)
        grid = [[0]*n for _ in range(m)]
        islands = [] # List of Sets where each set is a connected component
        out = []
        for r,c in positions:
            new_vertex = get_vertex(r, c)
            if grid[r][c] == 0:
                add_vertex(new_vertex)
                grid[r][c] = 1
            for delta_r, delta_c in [(0,-1), (0,+1), (-1,0), (1,0)]:
                rr, cc = r + delta_r, c + delta_c
                if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == 1:
                    neighbor_vertex = get_vertex(rr, cc)
                    union_find(new_vertex, neighbor_vertex)
            out.append(len(islands))
        return out



"""
A much cleaner solution using standard DFU:
"""
class DFU():
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [0]*n
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            return self.find(self.parents[x])
    def union(self, x, y):
        xrep, yrep = self.find(x), self.find(y)
        if xrep == yrep:
            return 0
        else:
            if self.sizes[xrep] >= self.sizes[yrep]:
                self.sizes[xrep] += self.sizes[yrep]
                self.parents[yrep] = xrep
            else:
                self.sizes[yrep] += self.sizes[xrep]
                self.parents[xrep] = yrep
            return 1
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        islands = DFU(m*n)
        count_islands = 0
        res = []
        grid = [[0]*n for _ in range(m)]
        for r, c in positions:
            if grid[r][c] == 0:
                grid[r][c] = 1
                count_islands += 1
                for rr, cc in [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]:
                    if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == 1:
                        count_islands -= islands.union(r*n + c, rr*n + cc)
            res.append(count_islands)
        return res
