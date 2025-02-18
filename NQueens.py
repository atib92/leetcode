""" The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""

class Solution:
    """ 
    The idea is to try placing a queen in row[i] and recusively try to place the next queen in row[i+1].
    A successfull combination ends when we place the last queen in the last row.
    An unsuccessfull combination ends when we cannot place a queen in any row.

    We need to find all valid combinations, so irrespective if a placing queen in row[i][j] succeeds or not,
    we try next with row[i][j+1].
    """
    def _is_available(self, row, col, grid):
        for r in range(self.N):
            for c in range(self.N):
                if grid[row][c] == 'Q' or grid[r][col] == 'Q':
                    return False
                if grid[r][c] == 'Q' and abs(r-row) == abs(c-col):
                    return False
        return True
    def queen(self, row, n, grid):
        if n == 0:
            self.results.append(self.process_output(grid))
            return
        if row + n > self.N or row >= self.N:
            return None
        for col in range(self.N):
            if self._is_available(row, col, grid) is True: # Available cell
                grid[row][col] = 'Q'
                self.queen(row+1, n-1, grid)
                grid[row][col] = '.'
    def process_output(self, grid) -> int:
        """ 
        input: [[Q X X],[X X Q],[X Q X]]
        output: ['Q..', '..Q', '.Q.']        
        """
        ret = []
        for row in grid:
            s = ''.join(row)
            ret.append(s)
        return ret

    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.'] * n for _ in range(n)]
        self.results = []
        self.N = len(grid)
        self.queen(0,n,grid)
        return self.results
