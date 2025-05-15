"""
542. 01 Matrix
Solved
Medium
Topics
Companies
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Multi BFS:
        1. Start a BFS from each zero cell, enque (0, r, c) for each zero
        2. Deque all elements (distance, r, c) from the qeueu
        3. For each element, enqueue neighbor if its a 1 :
                1. Use r, c to find neighbors which are still 1
                2. enque (distance+1, r', c') 
                3. Everytime you convert a 1 to 0 and enque, DEC NUM_ONES
        4. Stop when queue is empty or NUM_ONES is zero i,e all ones have been processed
        5. Ans is the last/max distance in the enqueued node
        """
        q = deque()
        NUM_ONES = 0
        R, C = len(mat), len(mat[0])
        result = [[0]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 0:
                    q.append((0, r, c))
                else:
                    NUM_ONES += 1
        while(len(q) != 0 and NUM_ONES > 0):
            zeros = []
            while(len(q) != 0):
                zeros.append(q.popleft())
            for zero in zeros:
                distance, r, c = zero[0], zero[1], zero[2]
                for d_r, d_c in [(0, -1), (-1, 0), (0, +1), (+1, 0)]:
                    if 0 <= (r + d_r) < R and 0 <= (c + d_c) < C:
                        #print(f'R: {R} C: {C} r:{r} d_r:{d_r} c:{c} d_c:{d_c} distance:{distance}')
                        if mat[r+d_r][c+d_c] == 1:
                            q.append((distance+1, r+d_r, c+d_c))
                            result[r+d_r][c+d_c] = distance + 1
                            NUM_ONES -= 1
                            mat[r+d_r][c+d_c] = 0 # So that we do not process this agin.
        return result
