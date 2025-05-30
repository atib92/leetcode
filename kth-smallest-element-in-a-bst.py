"""
Kth Smallest Element in a BST
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def run(self, node, k):
            if not node or self.stop == True:
                return
            else:
                self.run(node.left, k)
                self.inorder.append(node.val)
                if self.index == k-1:
                    self.stop = True
                    return
                self.index += 1
                self.run(node.right, k)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Do an inorder traversal and return k-1th element 
        Time: O(K), stop when in-order traversal writes the kth element
        """
        self.inorder = []
        self.index = 0
        self.stop = False
        self.run(root, k)
        return self.inorder[k-1]
