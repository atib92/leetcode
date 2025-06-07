"""
 Top K Frequent Elements
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Frequency Counter + MaxHeap
        a. First Pass: Store (num, count) for each num in nums in a max heap. Heapify based on count (heapq default is a min heap, we save -count to use it as a max heap)
        b. Pop first K elements
        O(NlogN)
        """
        max_heap = []
        d = {}
        for num in nums:
            d[num] = d.get(num,0) + 1
        for num, count in d.items():
            heapq.heappush(max_heap, (-count, num))
        output = []
        while(k > 0):
            output.append(heapq.heappop(max_heap)[1])
            k -= 1
        return output

 def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Here we will maintain a k sized min-heap. At any point if the heap size gooes beyond k,
        we pop to bring it down. At the end the last k elements left in the min heap should be
        the top K elements. We just need to return in reverse order since its a min-heap
        This is O(KlogK)
        """
        min_heap = []
        d = {}
        for num in nums:
            d[num] = d.get(num,0) + 1
        for num, count in d.items():
            heapq.heappush(min_heap, (count, num))
            while(len(min_heap) > k):
                heapq.heappop(min_heap)
        return [elem[1] for elem in min_heap[-1::-1]]

