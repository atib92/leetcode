"""
Given a root of a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.

Examples:

Input: root[] = [1, 2, 3, 4, 5, 6, 7, N, N, N, N, N, 8, N, 9]
Vertical-Taversal-          
Output: [[4], [2], [1, 5, 6], [3, 8], [7], [9]]
"""
class Solution:
    def _verticalOrder(self, node, level):
        if node is not None:
            if level not in self._dB:
                self._dB[level] = [node.data]
            else:
                self._dB[level].append(node.data)
            self._verticalOrder(node.left, level-1)
            self._verticalOrder(node.right, level+1)
            
    def verticalOrder(self, root): 
        # Your code here
        self._dB = {}
        self._verticalOrder(root, 0)
        output = []
        for level in sorted(self._dB):
            output.append(self._dB[level])
        return output
