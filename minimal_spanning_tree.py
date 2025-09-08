"""
Minimal Spanning Tree using Prims Vs Kruskal's
"""
import heapq

class DSU():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def join(self, x, y):
        x_rep , y_rep = self.find(x), self.find(y)
        if x_rep != y_rep:
            if self.size[x_rep] >= self.size[y_rep]:
                self.parent[y_rep] = x_rep
                self.size[x_rep] += self.size[y_rep]
            else:
                self.parent[x_rep] = y_rep
                self.size[y_rep] += self.size[x_rep]
class Solution:
    def spanningTree(self, V, edges):
        #return self.spanningTreePrims(V, edges)
        return self.spanningTreeKruskals(V, edges)
    def spanningTreePrims(self, V, edges):
        # code here
        is_visited = [False] * V
        visited_nodes = set([0])
        is_visited[0] = True
        c = 1
        heap = []
        adj_matrix = [[None]*V for _ in range(V)]
        wt = 0
        for src, dst, w in edges:
            adj_matrix[src][dst] = w
            adj_matrix[dst][src] = w
        for dst in range(V):
            if adj_matrix[0][dst]:
                heapq.heappush(heap, (adj_matrix[0][dst], dst))
        while(heap):
            w, v = heapq.heappop(heap)
            if is_visited[v] == False:
                is_visited[v] = True
                wt += w
                c += 1
                if c == V:
                    break
                for dst in range(V):
                    if adj_matrix[v][dst]:
                        heapq.heappush(heap, (adj_matrix[v][dst], dst))
        return wt
    def spanningTreeKruskals(self, V, edges):
        """
        Unlike Prims which grows one tree, kruskal's algorithm grows a forest.
        """
        dsu = DSU(V)
        edges = sorted(edges, key=lambda x:x[2])
        wt = 0 # Running wt of mst
        c = 0 # No of edges added
        for src, dst, w in edges:
            if dsu.find(src) != dsu.find(dst):
                wt += w
                c += 1
                if c == V-1:
                    break
                dsu.join(src, dst)
        return wt
