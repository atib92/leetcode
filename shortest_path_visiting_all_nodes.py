"""
Source : https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/?envType=problem-list-v2&envId=graph 
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.
Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
"""
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        Algo: Multi BFS
        We start a BFS from all nodes:
        1. Enque nodes at level 0 (All nodes)
        2. Deque all nodes and enque all its connected nodes (All level 1 nodes)
        3. At every time we need to track what the nodes have been already visited as part of that BFS so probably enque the [node, [list of parent nodes]] in the queue.
        4. Even as part of the same BFS, a node can be visited multiple times. Think of cases when a path leads to end of the graph and you need to come back to a middle node
           to explore remaining paths (a-b-c) so the path here can look like a->b->c->b->d
                                         |
                                         d
        5. Think of multi-bfs as N BFS instance running parallely. The first BFS that is able to visit all nodes is definitely the one that has the shortest path that touches all nodes and
           the last level of that BFS is the length of that path.
        6. Optimizations:
           i. We said we need to enque the path along side the nodes but that is very memory heavy. Since we do not care about the exact path but only what nodes are part of the path, we can use
              bit masking. E.g: Represent N nodes with N bits where if ith bit is set, we know node i has been visited.
              Marking : To mark bit i, just set the ith bit : 1 << i | path_info
           ii. path_info starts with all bit except the starting point of that bfs set. Ex. bfs-j starts with path info (1 << j)
           iii. There is just one more issue. In point 4 we talked about how the same node can be traversed multiple times b->c and then back c->b. We need to make sure we do not get caught
                up in an infinite loop between b<->c. To avoid this we need to make sure if had reached 'b' with path_info "X" and decided to go 'c' , when
                we come back to 'b' from 'c', we do not again go to 'c'. This can be done by caching the path_info (the state) along side 'b' when we had decided to go to 'c' (marking bit c).
                So the next time we are at 'b'. We know from the path_info / state cache that we had been at 'b' with exactly the same state before, so we can avoid that path.
           iv. The state can be a dict with nodes as keys and a list of all states seen so far. But the code was not performant and was failing some testcase at scale. To make the lookup
               effecient, changed the dict keys from a list to a set. (With lists, the runtime of high scale test cases was ~3.7s and that came down to 90ms with sets)
               For more on this check: List Vs Sets in python for lookup operations. Hint: Sets use hash to store elements.
        """
        q = deque()
        N = len(graph)
        stop = pow(2,N) - 1 # Path info with all bits sets !
        visited = {}
        for node in range(N):
            q.append((node, 1 << (node)))
            visited[node] = set() # [] (Note: See 6.iv above)
        steps = 0
        while(len(q) != 0):
            size = len(q)
            for _ in range(size):
                # Need to dequeue all noddes at level 'K' before enqueing level 'K+1' nodes. (i,e across all BFS instances)
                node, path = q.popleft()
                if path == stop:
                    return steps
                else:
                    for next_node in graph[node]:
                        next_state = path | (1 << (next_node))
                        if next_state not in visited.get(next_node):
                            q.append((next_node, next_state))
                            visited[next_node].add(next_state)
            steps += 1
