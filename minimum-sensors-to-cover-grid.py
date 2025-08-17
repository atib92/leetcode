"""
Minimum Sensors to Cover Grid
Solved
Medium
Hint
You are given n × m grid and an integer k.

A sensor placed on cell (r, c) covers all cells whose Chebyshev distance from (r, c) is at most k.

The Chebyshev distance between two cells (r1, c1) and (r2, c2) is max(|r1 − r2|,|c1 − c2|).

Your task is to return the minimum number of sensors required to cover every cell of the grid.

 

Example 1:

Input: n = 5, m = 5, k = 1

Output: 4

Explanation:

Placing sensors at positions (0, 3), (1, 0), (3, 3), and (4, 1) ensures every cell in the grid is covered. Thus, the answer is 4.

Example 2:

Input: n = 2, m = 2, k = 2

Output: 1

Explanation:

With k = 2, a single sensor can cover the entire 2 * 2 grid regardless of its position. Thus, the answer is 1.

 

Constraints:

1 <= n <= 103
1 <= m <= 103
0 <= k <= 103
"""
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        """
        k = 1 case
          0 1 2 3 4
        0 . . . . .
        1 . X X X .
        2 . X 1 X .
        3 . X X X .
        4 . . . . .
        
        So if you think about it a Chebyshev distance of 'k' from a cell (r,c) is a square
        centerd at (r,c) with side length of 2*K+1.
        Now in a n*m grid, what is the minimum number of such squares we can fit to cover each cell of the grid,

        For n rows, we need atleast n / (2k + 1) (rounded to next integer, hence use ceiling function)
        For m cols, we need atleast m / (2k + 1) (ditto)
        For every covered square along the rows, we need as many squares for the columns, hence multiply the results.
        """
        l = 2*k + 1
        return ceil(n / l) * ceil(m/l)
