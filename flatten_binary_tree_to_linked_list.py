"""
Flatten Binary Tree to Linked List
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        _flatten shd return the last node (tail of the linked list) so that the linked list can be extended

        Time: O(N) Same as Pre Order Traversal
        SpaceL: O(1) Everything is inplace
        """
        def _flatten(node):
            if node.left is None and node.right is None:
                # Leaf node
                return node
            else:
                # node has either / both left and right sub tree
                node_left, node_right = node.left, node.right
                f_left, f_right = None, None
                if node.left:
                    f_left = _flatten(node.left)
                if node.right:
                    f_right = _flatten(node.right)
                # Adjustments
                if f_left:
                    node.right = node.left
                    f_left.right = node_right #f_right
                node.left = None
                if f_right:
                    return f_right
                elif f_left:
                    return f_left
                else:
                    return node
        if root:
            return _flatten(root)

