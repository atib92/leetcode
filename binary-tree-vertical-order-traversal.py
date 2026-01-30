'''
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder_v1(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = deque()
        nodes.append((root, 0))
        level_db = {}
        while nodes:
            node, level = nodes.popleft()
            if node is not None:
                level_info = level_db.get(level, [])
                level_info.append(node.val)
                level_db[level].append(node.val)
                if node.left is not None:
                    nodes.append((node.left, level-1))
                if node.right is not None:
                    nodes.append((node.right, level+1))
        output = []
        for key in sorted(level_db.keys()):
            output.append(level_db[key])
        return output
    
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Better version of the above using defaultdict to avoid get method
        and tracking min_level and max_level to avoid sorting at the end
        Core idea remains the same: BFS traversal with level tracking
        '''
        if not root:
            return []
        nodes = deque()
        nodes.append((root, 0))
        level_db = defaultdict(list)
        min_level, max_level = 0, 0
        while nodes:
            node, level = nodes.popleft()
            min_level = min(level, min_level)
            max_level = max(level, max_level)
            level_db[level].append(node.val)
            if node.left is not None:
                nodes.append((node.left, level-1))
            if node.right is not None:
                nodes.append((node.right, level+1))
        output = []
        for key in range(min_level, max_level+1):
            output.append(level_db[key])
        return output