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
