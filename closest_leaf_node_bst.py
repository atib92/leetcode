"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
"""

from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Optimal BFS : Bread First Search goes level by level so is way more efficient than Depth First Search
        """
        Q = deque()
        if root is None:
            return 0
        else:
            Q.append((root,1))
            while(len(Q) != 0):
                node, depth = Q.popleft()
                if node.left == None and node.right == None:
                    return depth
                else:
                    if node.left is not None:
                        Q.append((node.left, depth+1))
                    if node.right is not None:
                        Q.append((node.right, depth+1))


    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        DFS : Depth first search is an overkill for this problem
        """
        if root is None:
            return 0
        else:
            print(f'{root.val}')
            left = right = False
            if root.left is not None:
                l_d = self.minDepth(root.left)
                left = True
            if root.right is not None:
                r_d = self.minDepth(root.right)
                right = True
            if left == True and right == True:
                return 1 + min(l_d, r_d)
            elif left == True:
                return 1 + l_d
            elif right == True:
                return 1 + r_d
            else:
                return 1
"""
Runtime comparision of DFS and BFS
BFS: 3 ms 50.4 MB
DFS: 170 ms 50.4 MB
BFS completes much faster since it goes level by level and return the moment it sees the first leaf node which is guranteed to be the closet leaf node.
DFS on the other hand has to explore each path till completion.
"""
