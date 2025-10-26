"""
You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

ui is the source node (an integer from 1 to n)
vi is the target node (an integer from 1 to n)
ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.

Example 1:



Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

Output: 3
Example 2:

Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2

Output: -1
Constraints:

1 <= k <= n <= 100
1 <= times.length <= 1000
"""
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Standard Dijkstras algorithm.
        """
        adj = {}
        for node in range(n):
            adj[node] = {}
        for src, dst, weight in times:
            adj[src-1][dst-1] = weight
        heap = [(0, k-1)]
        times = [float("inf")] * n
        min_time = 0
        count = 0
        while(heap and count < n):
            time, node = heapq.heappop(heap)
            if times[node] == float("inf"):
                min_time = max(min_time, time)
                count += 1
                times[node] = time
                for dst, w in adj[node].items():
                    if time+w < times[dst]:
                        heapq.heappush(heap, (time+w, dst))
        if count == n:
            return min_time
        else:
            return -1
