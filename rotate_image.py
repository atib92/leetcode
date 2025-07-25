"""
Rotate Image
Solved
Medium
Topics
conpanies icon
Companies
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

"""
Intuition
You can imagine the transformations happening in concentric circles. No. of concentric circle = n // 2 (Observation !)
Each concentric circle transforms all the cells starts from 'circle_index' to 'N - circle_index - 1'
Each transformatoin is 4 step is a 4 step transformation loop that runs like the following: (a, b) -> (c, d) -> (e, f) -> (g, h) ---> (a, b) where each transformation is consecutive tranformation is like : (r, c) -> (c, n-1-r)
Complexity
Time complexity:
O(M*M)

Space complexity:
O(1) No extra space required

Code
"""

class Solution:
    def rotate(self, grid: List[list[int]]) -> None:
        N = len(grid)
        num_circles = N // 2
        for circle_index in range(num_circles):
            def get_next(row, col):
                return col, N-1-row
            r = circle_index
            for c in range(circle_index, N - circle_index - 1):
                current_cell = (r, c)
                next_cell = get_next(r, c)
                value = grid[current_cell[0]][current_cell[1]]
                for i in range(4):
                    # Save this value before over-writing
                    tmp = grid[next_cell[0]][next_cell[1]]
                    # overwrite now
                    grid[next_cell[0]][next_cell[1]] = value
                    current_cell = next_cell
                    next_cell = get_next(next_cell[0], next_cell[1])
                    # Update value for overwriting in the next iteration
                    value = tmp
        return
        
