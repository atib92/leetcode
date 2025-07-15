"""
Longest Path in a Directed Acyclic Graph
Difficulty: HardAccuracy: 38.15%Submissions: 6K+Points: 8
Given a Weighted Directed Acyclic Graph (DAG) and a source vertex s in it, find the longest distances from s to all other vertices in the given graph. Return the distance array,  in the distance array instead of passing INF you need to have INT_MIN driver will automatically update it to INF.

Examples :

Input: n = 3, m = 2, s = 0, edges[] = [[0,2,1],[0,1,1]]
Output: distance[] = [0,1,1]
Explanation: The shortest distance of vertex 1 from 0 is 1 and that of two is also 1.
Input: n = 6,m = 10, s = 1, edges[] = [[0,1,5],[0,2,3],[1,3,6],[1,2,2],[2,4,4],[2,5,2],[2,3,7],[3,5,1],[3,4,-1],[4,5,-2]]
Output: distance[] = [INF,0,2,9,8,10]
Explanation: The vertex zero is not reachable from vertex 1 so its distance is INF, for 2 it is 2, for 3 it is 9, the same goes for 4 and 5.
Expected Time Complexity: O(V+E)
Expected Auxiliary Space: O(V)


Constraints:
1 <= n <= 103
1<=m<=n*(n-1)/2
0<=edges[i][0],edges[i][1]
-100<=edges[i][2]<=100.
"""
from typing import List


from collections import deque


class Solution:
    def maximumDistance(self, v : int, e : int, src : int, edges : List[List[int]]) -> List[int]:
        """
        1. Do a topological sort (we use Kahn's algorithm)
        2. Dynamic Programming bottom up : Starting from src, traverse the graph and update distance if higher than current. 
        """
        adj = [[None] * v for _ in range(v)] # Better off with an adj list. Saves a ton of space for sparse matrices.
        in_deg = [0] * v
        q = deque()
        topo = deque()
        for src_node, dst_node, w in edges:
            adj[src_node][dst_node] = w
            in_deg[dst_node] += 1
        for node, count in enumerate(in_deg):
            if count == 0:
                q.append(node)
        while(q):
            node = q.popleft()
            for dst, w in enumerate(adj[node]):
                if w is None:
                    continue
                in_deg[dst] -= 1
                if in_deg[dst] == 0:
                    q.append(dst)
            topo.append(node)
        distance = [float("-inf")] * v
        distance[src] = 0
        # topo has the topologically sorted vertices  from left to right
        started = False
        while(topo):
            node = topo.popleft()
            if started == False and node != src:
                # Pop off nodes until we hit src since we are intersted in distances from src.
                continue
            else:
                started = True
                for d, w in enumerate(adj[node]):
                    if w is None:
                        continue
                    if distance[d] < distance[node] + w:
                        distance[d] = distance[node] + w
        return ["INF" if d == float("-inf") else d for d in distance]
