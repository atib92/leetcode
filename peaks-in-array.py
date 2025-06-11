"""
 Peaks in Array
Solved
Hard
Topics
premium lock icon
Companies
Hint
A peak in an array arr is an element that is greater than its previous and next element in arr.

You are given an integer array nums and a 2D integer array queries.

You have to process queries of two types:

queries[i] = [1, li, ri], determine the count of peak elements in the subarray nums[li..ri].
queries[i] = [2, indexi, vali], change nums[indexi] to vali.
Return an array answer containing the results of the queries of the first type in order.

Notes:

The first and the last element of an array or a subarray cannot be a peak.
 

Example 1:

Input: nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]]

Output: [0]

Explanation:

First query: We change nums[3] to 4 and nums becomes [3,1,4,4,5].

Second query: The number of peaks in the [3,1,4,4,5] is 0.

Example 2:

Input: nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]]

Output: [0,1]

Explanation:

First query: nums[2] should become 4, but it is already set to 4.

Second query: The number of peaks in the [4,1,4] is 0.

Third query: The second 4 is a peak in the [4,1,4,2,1].

 

Constraints:

3 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i][0] == 1 or queries[i][0] == 2
For all i that:
queries[i][0] == 1: 0 <= queries[i][1] <= queries[i][2] <= nums.length - 1
queries[i][0] == 2: 0 <= queries[i][1] <= nums.length - 1, 1 <= queries[i][2] <= 105
"""
class Solution:
    """
    Since we are required to compute range queries, we approach the problem using segment tree. Segment
    tree will allow us to compute range queries in logN.

    Step1: Give the original input 'nums', build the peak array. 
    Step2: Using the peak array from Step-1 build a segment tree s.t that we can execute a range query between l and r to compute the number of peaks between l and r.
           Note: In as defined in the question, a range (l,r) is an open interval so you should account for that in computing the range query. We do that by computing range_query(l+1,r-1) since segment tree range intervals are closed [l,r]
    Step3: Use the segment tree to return the results  of range queries in O(NlogN)
    Step4: When the input array is changed at index "index", it potentially alters the peaks at index-1, index, index+1. Check and edit these 3 indices for peaks.
    Step5: For the above 3 indices, you also need to update the segment tree, this is done as follows:
           i. Say peak[k] has changed.
           ii. This would potentially change the range_query results for all ranges that includes the index 'k'
           iii. We update all such ranges recursively, as follows:
                 a. update(segment_tree_index,left,right,k)
                 b. recursive call either update(2*segment_tree_index+1, left, mid, k) or update(2*segment_tree_index+2, mid+1, r, k) depending on wher k falls in the (l,mid) and (mid+1,r) partition
                 c. Base condtion: if l==r, set segment_tree[segment_tree_index] = peak[k]
                 d. Remember to udpate segment_tree[segment_tree_index]
    """
    def build_peaks(self):
        for i in range(1, self.N-1):
            self.peaks[i] = 1 if self.nums[i] > max(self.nums[i-1], self.nums[i+1]) else 0
    def _adjust_segment_tree(self, s_index, l, r, p_index):
        """
        s_index: segment_tree index p_index: peak index / index in nums
        """
        if l == r:
            self.tree[s_index] = self.peaks[p_index]
        else:
            """ 
            Draw out the recursions in a papr to understand this !
            Basically if you draw out the segment tree, you will see that the leaf nodes are basically the elements in the peak array,
            E.g the node tracking the range [4,4] is nothing but peak[4]. So if you have to start from the root node of the segment
            tree and want to reach the leaf node which tracks the range [p_index, p_index] you have to choose between left and right
            children of the node in the following way:
            """
            mid = (l+r)//2
            if p_index <= mid:
                self._adjust_segment_tree(2*s_index+1,l,mid,p_index)
            else:
                self._adjust_segment_tree(2*s_index+2,mid+1,r,p_index)
            self.tree[s_index] = self.tree[2*s_index+1] + self.tree[2*s_index+2]
            
    def _build_segment_tree(self, index, l, r):
        if l == r:
            self.tree[index] = self.peaks[l]
        elif l < r:
            mid = (l + r) // 2
            left = self._build_segment_tree(2*index+1, l, mid)
            right = self._build_segment_tree(2*index+2, mid+1, r)
            self.tree[index] = left + right
        return self.tree[index]
    def build_segment_tree(self):
        # Use self.peaks to (re)build self.tree
        self._build_segment_tree(0,0,self.N-1)
    def _range_query(self, index, l, r, L, R):
        # index takes care for range [L, R] but we are interested in [l,r]
        if l <= L and r >= R:
            return self.tree[index]
        elif l > R or r < L:
            return 0
        else:
            mid = (L + R) // 2
            left = self._range_query(2*index+1, l, r, L, mid)
            right = self._range_query(2*index+2, l, r, mid+1, R)
            return left + right
    def range_query(self, l, r):
        # Range query [l,r] on the self.tree
        if l <= r:
            return self._range_query(0, l,r,0,self.N-1)
        else:
            return 0
    def _adjust_peak(self, index):
        self.peaks[index] = 1 if self.nums[index] > max(self.nums[index-1], self.nums[index+1]) else 0
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        self.N = len(nums)
        self.nums = nums
        self.peaks = [0] * self.N
        self.build_peaks()
        self.tree = [0] * (4*self.N)
        output = []
        self.build_segment_tree()
        for q in queries:
            if q[0] == 1:
                # Type 1: Determined the count of peak elements between l and r
                l = q[1]
                r = q[2]
                #print(f'Range Query on [{l}, {r}] Segment Tree {self.tree}')
                output.append(self.range_query(l+1, r-1))
            elif q[0] == 2:
                # Type 2: Change nums[index] to value
                index = q[1]
                value = q[2]
                self.nums[index] = value
                # change in 'index' affect peaks[index-1], peaks[index], peaks[index+1]
                for i in [-1,0,+1]:
                    if index+i > 0 and index+i < self.N-1:
                        self._adjust_peak(index+i)
                        self._adjust_segment_tree(0, 0, self.N-1, index+i)
                # todo(atib): Can we do something better than this to rebuild segment tree ?
                #self.build_segment_tree()
        return output
