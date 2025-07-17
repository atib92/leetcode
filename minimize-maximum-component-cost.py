"""
You are given an undirected connected graph with n nodes labeled from 0 to n - 1 and a 2D integer array edges where edges[i] = [ui, vi, wi] denotes an undirected edge between node ui and node vi with weight wi, and an integer k.

You are allowed to remove any number of edges from the graph such that the resulting graph has at most k connected components.

The cost of a component is defined as the maximum edge weight in that component. If a component has no edges, its cost is 0.

Return the minimum possible value of the maximum cost among all components after such removals.

 

Example 1:

Input: n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 2

Output: 4
"""
lass DSU(object):
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.count = n
    def find(self, v):
        parent = self.parent[v]
        if v != parent:
            root_parent = self.find(parent)
            # path compression
            self.parent[v] = root_parent
        return self.parent[v]
    def join(self, n, m):
        n_parent, m_parent = self.find(n), self.find(m)
        if n_parent != m_parent:
            if self.size[n_parent] > self.size[m_parent]:
                self.parent[m_parent] = n_parent
                self.size[n_parent] += self.size[m_parent]
            else:
                self.parent[n_parent] = m_parent
                self.size[m_parent] += self.size[n_parent]
            self.count -= 1
        return self.count
class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        """
        The idea is to go in reverse order adding edges, i.e, start with N components and add edges greedily. (Like Kruskal's)
        The firt edge that reduces the num components to k is the minimum edge weight which can be the maximum component cost
        for all graphs that will have <= k connected components 
        """
        if n <= k:
            return 0
        edges = sorted(edges, key=lambda x: x[2])
        dsu = DSU(n)
        for src, dst, w in edges:
            if dsu.join(src, dst) == k:
                return w
