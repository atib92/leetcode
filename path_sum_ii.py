"""
Path Sum II
Solved
Medium
Topics
conpanies icon
Companies
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Binary Tree | targeSum | Return all paths a.k.a pathInfo
        Recusion with path info but better:
        [Future]Recursion only propagates path info bottom up so that we only pass pathInfo for successfull paths/
        Future since multiple reverse paths from a node might match so the return list might compound
        Node value can be -ves so only stopping criteria are leaf nodes with pending targetSum 
        """
        def findPathSum(node, target, pathInfo):
            if node is not None:
                #print(f'fps {node.val} target {target} {pathInfo}')
                if node.left is None and node.right is None:
                    if node.val == target:
                        paths.append(pathInfo + [node.val])
                else:
                    findPathSum(node.left, target - node.val, pathInfo + [node.val])
                    findPathSum(node.right, target - node.val, pathInfo + [node.val])
        paths = []
        findPathSum(root, targetSum, [])
        return paths
