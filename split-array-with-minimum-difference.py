"""
Split Array With Minimum Difference
Solved
Medium
Hint
You are given an integer array nums.

Split the array into exactly two subarrays, left and right, such that left is strictly increasing and right is strictly decreasing.

Return the minimum possible absolute difference between the sums of left and right. If no valid split exists, return -1.

 

Example 1:

Input: nums = [1,3,2]

Output: 2

Explanation:

i	left	right	Validity	left sum	right sum	Absolute difference
0	[1]	[3, 2]	Yes	1	5	|1 - 5| = 4
1	[1, 3]	[2]	Yes	4	2	|4 - 2| = 2
Thus, the minimum absolute difference is 2.

Example 2:

Input: nums = [1,2,4,3]

Output: 4

Explanation:

i	left	right	Validity	left sum	right sum	Absolute difference
0	[1]	[2, 4, 3]	No	1	9	-
1	[1, 2]	[4, 3]	Yes	3	7	|3 - 7| = 4
2	[1, 2, 4]	[3]	Yes	7	3	|7 - 3| = 4
Thus, the minimum absolute difference is 4.

Example 3:

Input: nums = [3,1,2]

Output: -1

Explanation:

No valid split exists, so the answer is -1.

 

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= 105
"""

"""
contigous !!
[1 3 2]
[1]
[3 2]

[1 3]
[2]

[1 2 4 3]
[1 2]
[4 3]

[1 2 4]
[3]

Possible split positions 'n-1'
A split position i is valid if [0,i] [i+1, n-1] is valid (strictly increasing and strictly decreasing)
The trick is to find out strictly increasing and strictly decresingly efficiently (other wise O(N^2))

Say split i : sub arrays [0, i] and [i+1, n-1]
SubArray [0,i] is valid only if [0,i-1] was valid and nums[i] > nums[i-1]
SubArray [i+1,n-1] is valid only if [i,n-1] was valid and nums[i+1] < nums[i]
Step 1: Pre Compute the validity at split from i = 0 to n-2 : O(N)
Step 2: Pre compute prefix sum so that sum(nums([0,i])) and sum(nums[i+1,n-1]) is done in O(N)
Step 3: Traversal and if split at i is valid, compare and set max.


Time: O(N)
Space: O(N)
"""
class Solution:
    def print(self, s:str):
        #print(s)
        pass
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        split = 0
        prefix_subarray_validity = [False] * n
        prefix_subarray_sum = [0] * n
        suffix_subarray_validity = [False] * n
        suffix_subarray_sum = [0] * n
        # Bootstrapping: First element is strictly increasing, Last element is strictly decreasing
        prefix_subarray_validity[0] = suffix_subarray_validity[-1] = True
        prefix_subarray_sum[0], suffix_subarray_sum[-1] = nums[0], nums[-1]
        # Prefix subarray processing
        for i in range(1, n-1):
            # First subarray end at index 'i'
            prefix_subarray_validity[i] = (prefix_subarray_validity[i-1] == True and nums[i] > nums[i-1])
            prefix_subarray_sum[i] = prefix_subarray_sum[i-1] + nums[i]
        # Suffix subarray processing
        for j in range(n-2,-1,-1):
            # Second subarray starts at j
            suffix_subarray_validity[j] = (suffix_subarray_validity[j+1] == True and nums[j] > nums[j+1])
            suffix_subarray_sum[j] = suffix_subarray_sum[j+1] + nums[j]
        abs_diff = float("inf")
        # Checking splits
        for split in range(n-1):
            # First subarray ends at index split and second subarray starts at idnex split+1
            if prefix_subarray_validity[split] == True and suffix_subarray_validity[split+1] == True:
                abs_diff = min(abs_diff, abs(prefix_subarray_sum[split]-suffix_subarray_sum[split+1]))
        if abs_diff == float("inf"):
            return -1
        else:
            return abs_diff

