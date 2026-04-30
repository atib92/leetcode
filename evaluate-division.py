'''
399. Evaluate Division
Solved
Medium
Topics
conpanies icon
Companies
Hint
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
'''
from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        Treat each variable as a graph node
        when a/b = v, create couple of edges:
            i. a->b with weight v
            ii. b->a with weight 1/v
        Protocol: Divie by edge weight to from src to dst.
        So finally when traversing a path, just multiple the weights that will be SRC/DST i,e the query output
        A. Graph creation
        B. Graph traversal (not necessarily shortest path but just one path since we are guranteed
                            there are no contradictions.)
        '''
        def traverse(src, dst):
            '''
            Start from src and try to reach dst using adj.
            Key Points: Try all paths, Keep a track of nodes in a path to avoid loops
            '''
            q = deque()
            visited = set()
            q.append((src, 1))
            visited.add(src)
            while(q):
                node, cost = q.popleft()
                if node == dst:
                    return cost
                else:
                    for next_node, w in adj[node]:
                        if next_node not in visited:
                            visited.add(next_node)
                            q.append((next_node, cost * w))
            return -1.0

        adj = defaultdict(list)
        n = len(equations)
        for i in range(n):
            src, dst, w = equations[i][0], equations[i][1], values[i]
            adj[src].append((dst, w))
            adj[dst].append((src, float(1/w)))
        # query evaluation
        output = []
        for src, dst in queries:
            if src in adj and dst in adj:
                output.append(traverse(src, dst))
            else:
                output.append(-1.0)
                continue
        return output
















