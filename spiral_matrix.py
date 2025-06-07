"""
Spiral Matrix
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


"""
Intuition
We follow a simple protocol [right, down, left, up]
At any time, we have the "last" direction which could be any of the above four directions and depending on the matrix boundaries we try out all four directions with wrapping around the edge. Eg. If the last direction was down, we will try to continue down but if we cannot we will try the next direction in order which is left and so on...

This is achived by the (last + 1) % 4 in "next".

If the traversal changes the original direction, say you were approaching from right but can no longer go right and change to down. We also return the lastes direction so that subsequent traversals can be in the new direction.

Complexity
Time complexity:
O(N*M) since we touch each cell.
Space complexity:
O(N*M) since I am using a visited matrix but if its allowed to mangle the matrix, you could achive this w/o the extra matrix at O(1)
"""
class Solution:
    def next(self, r, c, last, R, C, visited):
        """
        Protocol: 
        [0-right, 1-down, 2-left, 3-up]
        Starting from moves[last] try all four moves
        """
        moves = [(r,c+1),(r+1,c),(r,c-1),(r-1,c)]
        attempts = 4
        while(attempts > 0):
            next_r, next_c = moves[last][0], moves[last][1]
            if 0 <= next_r < R and 0 <= next_c < C and visited[next_r][next_c] == False:
                return last, next_r, next_c
            else:
                attempts -= 1
                last = (last + 1) % 4
        return None, None, None
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        out = [matrix[0][0]]
        r, c = 0, 0
        visited = [[False]*C for _ in range(R)]
        visited[0][0] = True
        last = 0
        while(len(out) < R*C):
            last, r, c = self.next(r, c, last, R, C, visited)
            if r is not None and c is not None:
                out.append(matrix[r][c])
                visited[r][c] = True
        return out
