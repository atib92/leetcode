"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Algo: Imagine the array in its final sorted (ascending) form. 
              The last 'K' elements would be starting from 'K'th maximum to largest element
              The first 'K-1' elements would be smaller than the 'K'the largest.
              That means if we somehow had a min heap of the k largest elements, the kth largest element will be the heap root.
              How do we build that heap : Remeber we need to delete all elements from the smallest to the Kth largest. This can be
              done if we maintain a k sized min-heap. Everytime the size of the heap exceed k, we delete an element. By definition,
              this will eliminate the smallest element at the time in the heap. So at the end we will be left with a k sized heap
              with elements from kth largest to largest and the kth largest at the root.

              Note: A similar logic can be applied for kth smallest/largest ... 

        """
        q = []
        for item in nums:
            heapq.heappush(q, item)
            if len(q) > k:
                heapq.heappop(q)
        return q[0]
    
 
 
     # ------------ Same Algorithm but with inhouse heap --------------
     def heapify_up(self, heap, index):
        """
        heapify at index
        """
        parent = (index - 1) >> 1
        if index > 0 and heap[parent] > heap[index]:
            heap[parent], heap[index] = heap[index], heap[parent]
            self.heapify_up(heap, parent) 

    def extract_min(self, heap):
        """
        return min-element i.e the heap root
        But heapify before returning
        """
        ret = heap[0]
        if len(heap) > 1:
            heap[0] = heap.pop()
            self.heapify_down(heap, 0)
        else:
            heap.pop()
        return ret
     
    def heapify_down(self, heap, index):
        left = (index << 1 ) + 1
        right = (index + 1) << 1
        if right < len(heap):
            if heap[left] < heap[right]:
                next_index = left
            else:
                next_index = right
        elif left < len(heap):
            next_index = left
        else:
            next_index = None
        if next_index is not None:
            if heap[index] > heap[next_index]:
                heap[index], heap[next_index] = heap[next_index], heap[index]
                return self.heapify_down(heap, next_index)
             
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Algo: Same algo but implementing the min-heap inhouse.
        """
        q = []
        for item in nums:
            q.append(item)
            self.heapify_up(q, len(q)-1)
            if len(q) > k:
                self.extract_min(q)
        return q[0]
