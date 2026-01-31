'''
Longest Line of Consecutive One in Matrix
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, or anti-diagonal.
'''
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        '''
        Maintain 4 matrices
        H, V, D, AD for horizontal, vertical, diagonal and anti-diagonal
        
        '''
        R, C = len(mat), len(mat[0])
        H, V, D, AD = [[0]*C for _ in range(R)], [[0]*C for _ in range(R)], [[0]*C for _ in range(R)], [[0]*C for _ in range(R)]
        longest_line = 0
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 1:
                    H[r][c] = V[r][c] = D[r][c] = AD[r][c] = 1
                    # Horizontal
                    if c > 0:
                        H[r][c] += H[r][c-1]
                    # Vertical
                    if r > 0:
                        V[r][c] += V[r-1][c]
                    # Diagonal
                    if r > 0 and c > 0:
                        D[r][c] += D[r-1][c-1]
                    # Anti Diagonal
                    if r > 0 and c < C-1:
                        AD[r][c] += AD[r-1][c+1]
                longest_line = max(longest_line, H[r][c], V[r][c], D[r][c], AD[r][c])
        return longest_line