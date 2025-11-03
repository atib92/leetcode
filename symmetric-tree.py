"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

SEE QUESTION FOR DIAGRAM

Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _func(node_X, node_Y):
            if not node_X and not node_Y:
                return True
            elif node_X and node_Y:
                if node_X.val != node_Y.val:
                    return False
                else:
                    return _func(node_X.left, node_Y.right) and _func(node_X.right, node_Y.left)
            else:
                return False
        return _func(root, root)
