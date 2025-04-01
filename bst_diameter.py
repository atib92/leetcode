"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def is_leaf(self, node):
        return node.right is None and node.left is None
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self._diameterOfBinaryTree(root)
        return self.diameter
    def _diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None or self.is_leaf(root):
            return 0
        else:
            left_diameter, right_diameter = 0, 0
            if root.left is not None:
                left_diameter = 1 + self._diameterOfBinaryTree(root.left)
            if root.right is not None:
                right_diameter = 1 + self._diameterOfBinaryTree(root.right)
            self.diameter = max(self.diameter, left_diameter + right_diameter)
            return max(left_diameter, right_diameter)
