"""
 Walls and Gates
Solved
Medium
Topics
conpanies icon
Companies
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
"""
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        Approach:
        1. We do a Multi BFS from each GATE.
        2. We only move to neighboring rooms which are still empty
        Note: BFS gurantees that a room that has been visited by a earlier GATE can not be visited with a smaller distance later. (Very much like stale oranges problems)\
        EDIT: We were earlier enqueuing the distance in the queue (r,c,d) but if you think of it, cells are enqueed/dequeued to/from the queue at the same level 'd' which is
        initially zero (for the gates) and increases as BFS goes layer by layer. So you can save memory by tracking 'd' outside the queue.
        """
        EMPTY = 2147483647
        WALL = -1
        GATE = 0
        R, C = len(rooms), len(rooms[0])
        q = deque()
        empty_rooms = 0
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == GATE:
                    q.append((r,c))
                elif rooms[r][c] == EMPTY:
                    empty_rooms += 1
        directions = [(0,-1),(0,+1), (-1,0), (+1,0)]
        d = 0 # distance to gate
        while(q and empty_rooms > 0):
            # Deque all cells
            nodes = []
            d += 1 # Everytime you deque, this is +1 distance away from a gate.
            while(q):
                nodes.append(q.popleft())
            for node in nodes:
                r, c = node[0], node[1]
                for rr, cc in directions:
                    r_bar, c_bar = r+rr, c+cc
                    if 0 <= r_bar < R and 0 <= c_bar < C and rooms[r_bar][c_bar] == EMPTY:
                        rooms[r_bar][c_bar] = d
                        empty_rooms -= 1
                        q.append((r_bar, c_bar, d+1))
        return
