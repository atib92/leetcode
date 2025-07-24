"""
Sudoku Solver
Hard
Topics
conpanies icon
Companies
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""

"""
Intuition
In Problems like these (e.g N Queens) you need to make a move (a move in this case is placing a digit in a sudoku cell) and try to move forward. If at any point you cannnot (No valid moves possible given the constraints of the problem). You need to revert already made moves and try again.

Approach
Recursively try placing digits in board(row, col). If moves are not possible or if a move leads to a future move to be impossible, backtrack and try other options.
"""

from typing import List

class Solution:
    """Utilities to get row and col values quickly
    Furture Optimization (A must for larger boards):
    Use State Caching i,e a separate datastructure for values in row 'i', col 'i' and grid 'i' for i in [0,9)
    self.rows = [set() for _ in range(9)]
    self.cols = [set() for _ in range(9)]
    self.grids = [set() for _ in range(9)] *
    Then you do not need to recompute values in "get_row(col)(grid)_values". All you need to do is check if
    potential 'elem' is NOT IN self.rows[row], NOT in self.cols[col] and NOT in self.grids[idx] *

    * We would need to map a cell (row, col) to an idx in the self.grids. We can thin of it as something like
    (row // 3)*3 + (col // 3)
   
    
    """
    def get_row_values(self, row: int) -> set[str]:
        return set([self.board[row][col] for col in range(9)])
    def get_col_values(self, col:int) -> set[str]:
        return set([self.board[row][col] for row in range(9)])
    def get_grid_values(self, row: int, col: int) -> set[str]:
        # Given any row, col find the grid center using the below formula
        # Once you have that, the grid values are the 3 X 3 grid around it
        grid_row = (row // 3) * 3 + 1
        grid_col = (col // 3) * 3 + 1
        ret = set()
        for rr in [-1, 0, +1]:
            for cc in [-1, 0, +1]:
                ret.add(self.board[grid_row+rr][grid_col+cc])
        return ret
    def place(self, row, col):
        print(f'Place ({row},{col})')
        #self.count += 1
        #if self.count > 100:
        #    print(f'Early Exit')
        #    return False
        if row > 8:
            # Nothing more to place.
            return True
        else:
            # We are still inside the grid
            if col > 8:
                print(f'Outside the Grid. Please check your code !')
                return False
            else:
                # We are safely inside the grid
                if self.board[row][col] == '.':
                    # We need to place
                    row_values = self.get_row_values(row)
                    col_values = self.get_col_values(col)
                    grid_values = self.get_grid_values(row, col)
                    taken = set.union(row_values, col_values, grid_values)
                    available = self.NUMS - taken
                    for elem in available:
                        # Try elem in this position
                        self.board[row][col] = elem
                        # If we are here, continue to the next cell for placement
                        if col + 1 > 8:
                            next_row, next_col = row+1, 0
                        else:
                            next_row, next_col = row, col+1
                        if self.place(next_row, next_col) == True:
                            return True
                        else:
                            # Reset and continue
                            self.board[row][col] = '.'
                            continue
                    # If we are here, we have not been able to place
                    return False
                else:
                    # Already placed
                    if col + 1 > 8:
                        next_row, next_col = row+1, 0
                    else:
                        next_row, next_col = row, col+1
                    return self.place(next_row, next_col)

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.NUMS = set([str(c+1) for c in range(9)])
        self.count = 0
        return self.place(0,0)
    
if __name__ == "__main__":
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    sol.solveSudoku(board)
    print(sol.board)
