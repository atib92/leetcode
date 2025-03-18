"""
Source : https://leetcode.com/problems/min-cost-to-connect-all-points/description/ 
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
"""
class Solution:
    def distance(self, src, dst):
        return abs(src[0]-dst[0]) + abs(src[1]-dst[1])

    def find_set(self, node, sets):
        # TODO: This can be improved by using a hash/dict instead.
        for index, _set in enumerate(sets):
            if node in _set:
                return index
        print(f'Cant find {node} in all sets {sets}')
        return None

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        The idea is to find a minimal spanning tree using Kruskal's algo.
        We build an adj list where each element is basically an edge (src_node, dst_node, manhatten_distance)
        Next we sort this list in ascending order of distance so that edges with lesser weight/distance come first.
        After that the problem boils down to doing a MST via Kruskal's.
        We use union-join to initialize each node as its own set and then we continue to pick edges from the adj
        list built earlier until we end up with a MST (i,e we end up with just one set with all nodes in it.)
        """
        N = len(points)
        adj = []
        for src in range(N):
            for dst in range(src+1, N):
                adj.append([src, dst, self.distance(points[src], points[dst])])
        # adj[i] = [3,5,12] means an edge from node 3 to node 5 of weight 12
        adj = sorted(adj, key=lambda x: x[2])
        # union find sets
        sets = [{node} for node in range(N)]
        # sum of all edges in any set
        sums = [0 for _ in range(N)]
        for edge in adj:
            src, dst, val = edge[0], edge[1], edge[2]
            src_set = self.find_set(src, sets)
            dst_set = self.find_set(dst, sets)
            if src_set == dst_set:
                continue
            else:
                # TODO: This can be deduped by putting it in a standalone function 
                if src_set < dst_set:
                    sets[src_set] = sets[src_set].union(sets[dst_set])
                    sums[src_set] += sums[dst_set] + val
                    sets.pop(dst_set)
                    sums.pop(dst_set)
                    if len(sets[src_set]) == N:
                        return sums[src_set]
                else:
                    sets[dst_set] = sets[dst_set].union(sets[src_set])
                    sums[dst_set] += sums[src_set] + val
                    sets.pop(src_set)
                    sums.pop(src_set)
                    if len(sets[dst_set]) == N:
                        return sums[dst_set]
        return 0
```
