"""
Is Graph Bipartite?
Solved
Medium
Topics
conpanies icon
Companies
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

 

Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

Constraints:

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
"""
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [None] * n
        q = deque()
        for node in range(n):
            # The graph might not be connected hence we need to iterate over all nodes to make sure all nodes are colored.
            if not colors[node]:
                colors[node] = +1
                q.append(node)
                while(q):
                    current_node = q.popleft()
                    for neighbor in graph[current_node]:
                        if colors[neighbor] == None:
                            # Color uncolored nodes with the opoosite color
                            colors[neighbor] = -1*colors[current_node]
                            q.append(neighbor)
                        elif colors[neighbor] == colors[current_node]:
                            # if the neighbor node is already colored with the same color, its a conflict.
                            return False
        return True
