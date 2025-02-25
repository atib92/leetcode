"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
class Solution:
    """ Traverse the grid linearly and everytime grid[r][c] matches word[0] i,e the world can potentially start from here,
        start a DFS. DFS continues by matching the subsequent chars and end either when the word is found or you finish
        going through the grid.
        Note: To avoid traversing the same cell multiple times in the context of a path, we mangle the value of that cell
        and restore it once that path is processed since a cell can appear across different paths.
    """
    def is_valid(self, row, col, board):
        return ((0 <= row < len(board)) and (0 <= col <len(board[0])))
    def dfs(self, row, col, board, word):
        """ Starting from board[row][col] spawn further dfs in all possible directions.
        """
        if self.done is True:
            return
        elif len(word) == 0:
            self.done = True
            return
        else:
            for _r, _c in [(row-1, col),(row+1, col),(row, col-1),(row, col+1)]:
                if self.is_valid(_r, _c, board) and board[_r][_c] == word[0]:
                    save = board[_r][_c]
                    board[_r][_c] = "-"
                    self.dfs(_r, _c, board, word[1:])
                    board[_r][_c] = save
        return
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        self.done = False # Global Marker to stop all pending/ongoing recursions.
        for row in range(R):
            for col in range(C):
                if board[row][col] == word[0]:
                    save = board[row][col]
                    board[row][col] = "-"
                    self.dfs(row, col, board, word[1:])
                    board[row][col] = save
        return self.done
