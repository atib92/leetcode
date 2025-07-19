"""
Power Grid Maintenance
Solved
Medium
Topics
conpanies icon
Companies
Hint
You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).

These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or indirectly connected form a power grid.

Initially, all stations are online (operational).

You are also given a 2D array queries, where each query is one of the following two types:

[1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. If no operational station exists in that grid, return -1.

[2, x]: Station x goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type [1, x] in the order they appear.

Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

 

Example 1:

Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

Output: [3,2,3]

Explanation:



Initially, all stations {1, 2, 3, 4, 5} are online and form a single power grid.
Query [1,3]: Station 3 is online, so the maintenance check is resolved by station 3.
Query [2,1]: Station 1 goes offline. The remaining online stations are {2, 3, 4, 5}.
Query [1,1]: Station 1 is offline, so the check is resolved by the operational station with the smallest id among {2, 3, 4, 5}, which is station 2.
Query [2,2]: Station 2 goes offline. The remaining online stations are {3, 4, 5}.
Query [1,2]: Station 2 is offline, so the check is resolved by the operational station with the smallest id among {3, 4, 5}, which is station 3.
Example 2:

Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]

Output: [1,-1]

Explanation:

There are no connections, so each station is its own isolated grid.
Query [1,1]: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.
Query [2,1]: Station 1 goes offline.
Query [1,1]: Station 1 is offline and there are no other stations in its grid, so the result is -1.
 

Constraints:

1 <= c <= 105
0 <= n == connections.length <= min(105, c * (c - 1) / 2)
connections[i].length == 2
1 <= ui, vi <= c
ui != vi
1 <= queries.length <= 2 * 105
queries[i].length == 2
queries[i][0] is either 1 or 2.
1 <= queries[i][1] <= c
"""



"""
Intuition
The crux of the algorithm is to manange a DSU structure for power
grids. Each power grid is a connected component of the graph. The
additional operation required is to be able to do a maintainence
check on power stations for which we maintain min heaps.

Approach
Process the connections and create DSU for the power grids.
We mark offline nodes in a set. O(1) GETs if a power station is offline.
For each connected componenet, we maintain a min-heap structure. This allows us to get the minimum in a connected compoenent in O(1). We just need to ensure that offline nodes are pruned out the min-heap.
"""
import heapq


class DSU():
    def __init__(self, n: int):
        self.n = n
        # nodes are 1-based indexed
        self.parent = [i+1 for i in range(n)]
        self.size = [1] * n
    def find(self, n):
        parent = self.parent[n-1]
        if parent != n:
            rep = self.find(parent)
            # path compression
            self.parent[n-1] = rep
        return self.parent[n-1]
    def union(self, n, m):
        nrep, mrep = self.find(n), self.find(m)
        if nrep == mrep:
            return
        else:
            if self.size[nrep-1] > self.size[mrep-1]:
                self.parent[mrep-1] = nrep
                self.size[nrep-1] += self.size[mrep-1]
                self.size[mrep-1] = 0
            else:
                self.parent[nrep-1] = mrep
                self.size[mrep-1] += self.size[nrep-1]
                self.size[nrep-1] = 0
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        power_grid = DSU(c)
        for power_station_a, power_station_b in connections:
            power_grid.union(power_station_a, power_station_b)
        # Now that the connections are already made, we can create
        # a min heap structure for each connected components.
        connected_components = [[] for i in range(c)]
        for ps in range(1, c+1):
            rep = power_grid.find(ps)
            heap = connected_components[rep-1]
            heapq.heappush(heap, ps)
        offline = set()
        out = []
        for q_type, power_station in queries:
            if q_type == 1:
                # maintenance check
                res = -1
                if power_station not in offline:
                    res = power_station
                else:
                    rep = power_grid.find(power_station)
                    heap = connected_components[rep-1]
                    while(heap and heap[0] in offline):
                        heapq.heappop(heap)
                    if heap:
                        res = heap[0]
                out.append(res)
            elif q_type == 2:
                # offline
                offline.add(power_station)
            else:
                print(f'Unspported Query {q}')
                continue
        return out
