"""
Word Search in a 2D Grid of characters
Last Updated : 30 Sep, 2024
Given a 2D grid m*n of characters and a word, the task is to find all occurrences of the given word in the grid. A word can be matched in all 8 directions at any point. Word is said to be found in a direction if all characters match in this direction (not in zig-zag form).
The 8 directions are, Horizontally Left, Horizontally Right, Vertically Up, Vertically Down and 4 Diagonal directions.

Note: The returning list should be lexicographically smallest. If the word can be found in multiple directions starting from the same coordinates, the list should contain the coordinates only once. 
"""
#User function Template for python3
from collections import deque

class Solution:
    def bfs(self, r, c, d):
        q = deque()
        q.append((r, c, d, 0)) # row, col, direction, next index in word shd match
        while(q):
            r, c, d, idx = q.popleft()
            if self.grid[r][c] != self.word[idx]:
                return False
            else:
                idx += 1
                if idx == self.N:
                    return True
                else:
                    if d == 0:
                        r, c = r-1, c-1
                    elif d == 1:
                        r, c = r-1, c
                    elif d == 2:
                        r, c = r-1, c+1
                    elif d == 3:
                        r, c = r, c-1
                    elif d == 4:
                        r, c = r, c+1
                    elif d == 5:
                        r, c = r+1, c-1
                    elif d == 6:
                        r, c = r+1, c
                    elif d == 7:
                        r, c = r+1, c+1
                    else:
                        print(f'Invalid direction {d}')
                        return False
                    if 0 <= r < self.R and 0 <= c < self.C:
                        q.append((r, c, d, idx))
        return False
	def searchWord(self, grid, word):
	    """
	    Direction Protocol:
	    0 1 2
	    3 - 4
	    5 6 7
	    """
	    self.grid, self.word, self.N = grid, word, len(word)
		self.R, self.C = len(self.grid), len(self.grid[0])
		out = []
		for r in range(self.R):
		    for c in range(self.C):
		        for direction in range(8):
		            if self.bfs(r, c, direction) == True:
		                out.append((r,c))
		                break
		return out
