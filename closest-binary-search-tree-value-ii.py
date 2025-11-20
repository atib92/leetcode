"""
 Closest Binary Search Tree Value II
Solved
Hard
Topics
conpanies icon
Companies
Hint
Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

 

Example 1:


Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
Example 2:

Input: root = [1], target = 0.000000, k = 1
Output: [1]
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104.
0 <= Node.val <= 109
-109 <= target <= 109
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        """
        The problem becomes the same as find k closest elements to a target in a sorted array once you do the indorder traversal of the tree
        Time: O(N)
        """
        def inorder(node):
            if not node:
                return
            else:
                inorder(node.left)
                sorted_list.append(node.val)
                inorder(node.right)
        sorted_list = []
        inorder(root)
        # Find the first index > target
        n = len(sorted_list)
        l, r = 0, n - 1
        while(l < r and r < n):
            mid = (l + r) >> 1
            if sorted_list[mid] < target:
                l = mid + 1
            else:
                r = mid
        L, R = l-1, l
        out = []
        print(sorted_list)
        while(k > 0):
            if L < 0 and R >= n:
                break
            elif L < 0:
                out.append(sorted_list[R])
                R += 1
            elif R >= n:
                out.append(sorted_list[L])
                L -= 1
            elif abs(sorted_list[L]-target) <= abs(sorted_list[R]-target):
                out.append(sorted_list[L])
                L -= 1
            else:
                out.append(sorted_list[R])
                R += 1
            k -= 1
        return out
