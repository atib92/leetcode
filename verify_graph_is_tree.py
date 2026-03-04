#User function Template for python3

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    def find(self, x):
        xrep = self.parent[x]
        if x != xrep:
            self.parent[x] = self.find(xrep)
        return self.parent[x]
    def union(self, x, y):
        xrep, yrep = self.find(x), self.find(y)
        if xrep == yrep:
            return False
        else:
            if self.size[xrep] >= self.size[yrep]:
                self.size[xrep] += self.size[yrep]
                self.parent[yrep] = xrep
            else:
                self.size[yrep] += self.size[xrep]
                self.parent[xrep] = yrep
            return True

class Solution:
    def isTree(self, n, m, edges):
        # Code here
        graph = DSU(n)
        for i in range(m):
            if graph.union(edges[i][0], edges[i][1]) == False:
                return 0
            else:
                n -= 1
        if n == 1:
            return 1
        else:
            return 0
