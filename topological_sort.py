"""
Sample example from here : https://leetcode.com/discuss/general-discussion/1078072/introduction-to-topological-sort
"""

from collections import deque

# Good
# adj_info = {1:[2,4], 2:[3], 3:[], 4:[2,5,6], 5:[6], 6:[]}
# indegree = {1:0, 2:2, 3:1, 4:1, 5:1, 6:2}

# Bad
adj_info = {1:[2,4], 2:[3], 3:[4], 4:[2,5,6], 5:[6], 6:[]}
indegree = {1:0, 2:2, 3:1, 4:2, 5:1, 6:2}

done = []
NODES = 6
Q = deque()


def is_empty(q):
    return len(q) == 0

def get_unvisited_node_with_zero_indgree():
    for node, val in indegree.items():
        if node in done:
            continue
        else:
            if val == 0:
                return node
    return None

def decrement_indegree(node):
    # todo: Safeguard against invalid nodes (doesnt exist/ already zero cases)
    indegree[node] -= 1

Q.append(get_unvisited_node_with_zero_indgree())
while(is_empty(Q) == False):
    node = Q.popleft()
    # Reduce dependeny of each dependent nodes
    for dependent_node in adj_info.get(node, []):
        indegree[dependent_node] -= 1
        if indegree[dependent_node] == 0:
            Q.append(dependent_node)
    # mark this node as done
    done.append(node)

if len(done) == NODES:
    print('Topological sort completed. Result: {}'.format(done))
else:
    print('Cant finish Topological sort. Check graph for cycles. Partial results {}'.format(done))


"""
Output:

GOOD CASE:
Topological sort completed. Result: [1, 4, 2, 5, 3, 6]

BAD CASE:
Cant finish Topological sort. Check graph for cycles. Partial results [1]
"""
