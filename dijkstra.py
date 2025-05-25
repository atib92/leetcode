"""
Given an undirected, weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by 2d array edges[][], where edges[i]=[u, v, w] represents the edge between the nodes u and v having w edge weight.
You have to find the shortest distance of all the vertices from the source vertex src, and return an array of integers where the ith element denotes the shortest distance between ith node and source vertex src.

Note: The Graph is connected and doesn't contain any negative weight edge.

Examples:

Input: V = 3, edges[][] = [[0, 1, 1], [1, 2, 3], [0, 2, 6]], src = 2
Output: [4, 3, 0]
Explanation:

Shortest Paths:
For 2 to 0 minimum distance will be 4. By following path 2 -> 1 -> 0
For 2 to 1 minimum distance will be 3. By following path 2 -> 1
For 2 to 2 minimum distance will be 0. By following path 2 -> 2
"""
class Solution:
    """
    dijkstras is similar to bfs except that we use a priority queue (min heap)
    as opposed to a generici fifo heap as in BFS. The idea is to dequeu the
    node that is most favourable in the sense that allows the 'frontier' to be
    expanded with the least cost.
    """
    def dijkstra(self, V, edges, start):
        adj = [[] for _ in range(V)]
        for src, dst, cost in edges:
            adj[src].append((dst, cost))
            adj[dst].append((src, cost))
        visited = [float("inf")] * V
        visited[start] = 0
        pq = []
        heapq.heappush(pq, (0, start))
        while(pq):
            distance, node = heapq.heappop(pq)
            for dst, cost in adj[node]:
                updated_cost = distance + cost
                if visited[dst] >  updated_cost:
                    visited[dst] = updated_cost
                    heapq.heappush(pq, (updated_cost, dst))
        return visited
