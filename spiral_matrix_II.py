"""
Spiral Matrix II
Solved
Medium
Topics
conpanies icon
Companies
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
      """
      We iterate from 1 to n^2 and for each num, we try to find the next cell.
      The next cell logic is simple: We establish a priority right, down, left, up
      (the order of if-else in get_next establishes the priority). Give current
      cell and direction we return the next cell and direction.

      Time: O(n^2) [Actually 4*n^2 since at max we try 4 directions from each cell]
      """
        def get_next(r, c, d):
            attempt = 4
            while(attempt > 0):
                if d == 0:
                    rr, cc = r, c+1
                elif d == 1:
                    rr, cc = r+1, c
                elif d == 2:
                    rr, cc = r, c-1
                elif d == 3:
                    rr, cc = r-1, c
                if 0 <= rr < n and 0 <= cc < n and grid[rr][cc] is None:
                    return (rr, cc, d)
                else:
                    d = (d+1)%4
                    attempt -= 1
            return None
        grid = [[None] * n for _ in range(n)]
        r, c, d = 0, -1, 0
        for num in range(1, n*n + 1):
            cell = get_next(r, c, d)
            if cell is not None:
                r , c, d = cell[0], cell[1], cell[2]
                grid[r][c] = num
        return grid
