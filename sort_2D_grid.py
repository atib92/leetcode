"""
Young tableaus
An m X n Young tableau is an m X n matrix such that the entries of each row are
in sorted order from left to right and the entries of each column are in sorted order
from top to bottom.


Question: Given a Young Tableau (matrix where rows and columns are sorted), sort all elements
"""
class Solution:
    def left_child_index(self, index):
        return (index << 1) + 1
    def right_child_index(self, index):
        return (index + 1) << 1
    def parent_index(self, index):
        return index >> 1
    def min_child_index(self, arr, index):
        L = self.left_child_index(index)
        R = self.right_child_index(index)
        if R < len(arr):
            if arr[L] < arr[R]:
                return L
            else:
                return R
        elif L < len(arr):
            return L
        else:
            return None
    def heapify(self, heap, index):
        next_index = self.min_child_index(heap, index)
        if next_index is not None and heap[index] > heap[next_index]:
            heap[index], heap[next_index] = heap[next_index], heap[index]
            return self.heapify(heap, next_index)
    def extract_min(self, heap):
        ret = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            self.heapify(heap, 0)
        return ret
    def insert_new(self, heap, elem):
        heap.append(elem)
        index = len(heap)-1
        parent = self.parent_index(index)
        while(parent >= 0 and heap[parent] > heap[index]):
            heap[parent], heap[index] = heap[index], heap[parent]
            index, parent = parent, self.parent_index(parent)
    def sortedMatrix(self, N, Mat):
        """
        Algo: We use a min-heap to sort the young tableau.
        1. Create a min-heap with the first column of the matrix (the column is sorted so its already a min-heap)
        2. Continue the below steps until the heap is empty:
            i. extract_min and output the result. This finds the next smallest element.
            ii. During extract_min, you need to ensure you maintain the heap invariant. So add the last element of the heap to the root and heapify (the standard heap delete operation !)
            iii. Add the next element to the heap and heapify again (from left to root if required, again this is standard heap insertion operation)
            iv. How to find next element to add : We know the columns are sorted, so keep a track of the row, col of the last removed element and if that row has more element
                left, add the next element to the heap i,e row, col+1. This ensures we are adding the next smallest element to the heap and bubbling it up by the subsequent
                heapify.
        """
        heap = [ [Mat[row][0], row, 0] for row in range(N) ]
        res = []
        while(len(heap) > 0):
            val, row, col = self.extract_min(heap)
            res.append(val)
            if col+1 < N:
                self.insert_new(heap, [Mat[row][col+1], row, col+1])
        return res

if __name__ == "__main__":
    N, mat = 4, [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    sol = Solution()
    print(sol.sortedMatrix(N, mat))

"""
Output:
[10, 15, 20, 25, 27, 29, 30, 32, 33, 35, 37, 39, 40, 45, 48, 50]
"""


# Using standard lib

import heapq

class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, grid, K):
        # code here
        # return merged list
        R, C = len(grid), len(grid[0])
        pq = []
        for r in range(R):
            heapq.heappush(pq, (grid[r][0], r, 0))
        res = []
        while(pq):
            val, row, col = heapq.heappop(pq)
            res.append(val)
            if col + 1 < C:
                heapq.heappush(pq, (grid[row][col+1], row, col+1))
        return res
