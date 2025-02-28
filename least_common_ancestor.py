"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _get_path(self, root, node, path):
        if root is None:
            return None
        else:
            path.append(root)
            if root is node:
                return path
            else:
                l = self._get_path(root.left, node, path)
                if l is not None:
                    return l
                r = self._get_path(root.right, node, path)
                if r is not None:
                    return r
                path.remove(root)
                return None
    def _debug(self, p1):
        print([x.val for x in p1])
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        The idea is to is to track the path to each node and return the last node till which the path is common.
        """
        p1 = self._get_path(root, p, [])
        p2 = self._get_path(root, q, [])
        index = 0
        #self._debug(p1)
        #self._debug(p2)
        while(index < len(p1) and index < len(p2) and p1[index] == p2[index]):
            index += 1
        if index == len(p1):
            return p1[index-1]
        elif index == len(p2):
            return p2[index-1]
        else:
            return p1[index-1]
        return None

## Solution 2
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        elif root is p or root is q:
            return root
        else:
            l = self.lowestCommonAncestor(root.left, p, q)
            r = self.lowestCommonAncestor(root.right, p, q)
            if l and r:
                return root
            elif l is not None:
                return l
            elif r is not None:
                return r
            else:
                return None
