"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
class Solution:
    def _deserialize(self, index):
        return index // self.C, index % self.C
    def get(self, index: int) -> int:
        r,c = self._deserialize(index)
        return self.matrix[r][c]
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ The algo. is literally just a binary search with extra wrapper
            deserialization code that allows treating the 2D array as a 1D
            array.
        """
        self.R, self.C, self.matrix = len(matrix), len(matrix[0]), matrix
        low, high = 0, self.R*self.C - 1
        while(low <= high):
            mid = (low + high) // 2
            num = self.get(mid) # In a normal binary search, this is just num = mid but here we need to lookup in the deserialized matrix.
            if num == target:
                return True
            elif target > num:
                # In the right half
                low = mid + 1
            else:
                # In the left half
                high = mid - 1
        return False
