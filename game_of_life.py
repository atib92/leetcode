"""
https://leetcode.com/problems/game-of-life/description/

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.
"""
class Solution:
    def _check_neighbors(self, i, j, board, R, C):
        #print(f'{i}{j} Check {board}')
        directions = [[0,-1], [0,+1], [-1,-1], [-1,0],[-1,+1], [+1,-1], [+1,0], [+1,+1]]
        l, d = 0, 0
        for d_i, d_j in directions:
            ii, jj = i + d_i, j + d_j
            if 0 <= ii < R and 0 <= jj < C:
                if board[ii][jj] == 1 or board[ii][jj] == 3:
                    l += 1
                else:
                    d += 1
        return l, d
    def _set_final_state(self, i, j, l, d, board, R, C) -> None:
        #print(f'{i}{j} {l}{d} set board {board}')
        s = board[i][j]
        if s == 0:
            # If the cell is dead
            if l == 3:
                board[i][j] = 2
        else:
            # if the cell is alive
            if l < 2 or l > 3:
                board[i][j] = 3
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        We had 2 transition states that gets use the initial state and final state of any cells that change state.
        Do not return anything, modify board in-place instead.
        0: Dead
        1: Live
        2: 0->1 
        3: 1->0
        Rules:
        pass 1: treat 2 as a dead cell
                treat 3 as a live cell
        pass 2: Mark 2 as live
                Mark 3 as dead
        """
        R, C = len(board), len(board[0])
        for i in range(R):
            for j in range(C):
                l, d = self._check_neighbors(i, j, board, R, C)
                self._set_final_state(i, j, l, d, board, R, C)
        # 2nd pass
        for i in range(R):
            for j in range(C):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0
