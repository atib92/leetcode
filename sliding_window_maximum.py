"""
Sliding Window Maximum
Solved
Hard
Topics
conpanies icon
Companies
Hint
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""


# APPROACH 1
"""
We maintain a max heap and everytime the max element falls out of the running window we pop it. This way
we are sure the root of the heap falls inside the window and is the max because of the heap property
sum(logi) for i till N << NlogN i.e O(NlogN)
"""
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        N = len(nums)
        out = []
        l = 0
        r = 0
        for r in range(k):
            heapq.heappush(heap, (-1*nums[r], r))
        while(r < N):
            out.append(-1*heap[0][0])
            l += 1
            r += 1
            if r >= N:
                break
            while(heap and heap[0][1] < l): # We need to push the index also in the heap to be able to do this check.
                heapq.heappop(heap)
            heapq.heappush(heap, (-1*nums[r], r))
        return out


# APPROACH 2
"""
If we maintain a sorted list of window elements we can get the maximum in O(1).
Observation: This avoid having to sort elements. Whenever the window moves to the right, the new element
gurantess that any older elements in the window < new element can never be the window maxium since any
window those older elements will be in, the new element will also.
So, we can delete elements from the window that are smaller than the new element and maintain the window
to be sorted. At first this might seem this is N^2 since deleting old elements smaller than the new element
can seem O(N) but think about this: Every element is enqueued and dequeued only once from the deque making
the algorithm O(N)
"""
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # First insert the first K elements
        dq = deque()
        out = []
        n = len(nums)
        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i) # We only need to enqueu the indexes unlike the earlier heap solution.
        out.append(nums[dq[0]])
        for i in range(k,n):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            while(dq[0] < i - k + 1): # Make sure queue start doesn not have elems from earlier than window start
                dq.popleft()
            out.append(nums[dq[0]])
        return out 
