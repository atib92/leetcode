'''
Minimum Knight Moves
Solved
Medium
Topics
conpanies icon
Companies
Hint
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.
'''
from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        '''
        A Simple Multi BFS can solve the problem but a Bidirectional Multi BFS is much faster.
        '''
        directions = [
            (1,2),(1,-2), (-1,2), (-1,-2),
            (2,1),(2,-1),(-2,1),(-2,-1)
        ]
        steps_src, steps_dst = 0, 0
        q_src, q_dst = deque(), deque()
        visited_src, visited_dst = set(), set()
        visited_src.add((0,0))
        q_src.append((0,0))
        visited_dst.add((x,y))
        q_dst.append((x,y))
        while q_src or q_dst:
            # Expand the smaller frontier
            if len(q_src) <= len(q_dst):
                for _ in range(len(q_src)):
                    a, b = q_src.popleft()
                    if ((a,b) in visited_dst):
                        return steps_src + steps_dst
                    for dx, dy in directions:
                        if (a+dx,b+dy) not in visited_src:
                            q_src.append((a+dx, b+dy))
                            visited_src.add((a+dx, b+dy))
                steps_src += 1
            else:
                for _ in range(len(q_dst)):
                    a, b = q_dst.popleft()
                    if ((a,b) in visited_src):
                        return steps_src + steps_dst
                    for dx, dy in directions:
                        if (a+dx,b+dy) not in visited_dst:
                            q_dst.append((a+dx, b+dy))
                            visited_dst.add((a+dx, b+dy))       
                steps_dst += 1
        return None
