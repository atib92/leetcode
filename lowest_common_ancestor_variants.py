'''
 Lowest Common Ancestor of a Binary Tree
Solved
Medium
Topics
conpanies icon
Companies
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        elif root is p or root is q:
            return root
        else:
            # we are here means root is not p or q
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if left and right:
                return root
            else:
                # one of the calls wored i,e we either found one node in left or one node in right.
                # if we found one node in left and the no nodes in the right, we can safely assume
                # the other node is also in the left subtree at a lower level since we are guranteed
                # that both node exists.
                return left or right


'''
When nodes have a parent pointer to the parent
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
class Solution:
    def lowestCommonAncestor_v1(self, p: 'Node', q: 'Node') -> 'Node':
        '''
        Track the ancestral lineage of p. Do the same for q but at each
        step see if we discover an already seen ancestor.
        Time O(H)
        '''
        parent = set()
        while p:
            parent.add(p.val) # The question guranteed all values will be unique hence this suffices else we would need to store nodes and not just values.
            p = p.parent
        while q:
            if q.val in parent:
                return q
            else:
                parent.add(q.val) # We really do not need to save q's ancestor to the set, so remove this !
                q = q.parent
        return None
    def lowestCommonAncestor_v2(self, p: 'Node', q: 'Node') -> 'Node':
        '''
        Find merge point for linked list approach
        Find length lp: from p to root
        Find length lq: from q to root
        '''
        lp, lq = 0, 0
        np, nq = p, q
        while np:
            lp += 1
            np = np.parent
        while nq:
            lq += 1
            nq = nq.parent
        if lp >= lq:
            n1, n2 = p, q
        else:
            n1, n2 = q, p
        # n1 is the longer path
        delta = abs(lp-lq)
        while delta:
            delta -= 1
            n1 = n1.parent
        # Now continue until they merge
        while n1 and n2:
            if n1 == n2:
                return n1
            else:
                n1 = n1.parent
                n2 = n2.parent
        return None


        
