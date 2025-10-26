"""
Longest Balanced Subarray I
Solved
Medium
Topics
Hint
You are given an integer array nums.

A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.

 

Example 1:

Input: nums = [2,5,4,3]

Output: 4

Explanation:

The longest balanced subarray is [2, 5, 4, 3].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.
Example 2:

Input: nums = [3,2,2,5,4]

Output: 5

Explanation:

The longest balanced subarray is [3, 2, 2, 5, 4].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.
Example 3:

Input: nums = [1,2,3,2]

Output: 3

Explanation:

The longest balanced subarray is [2, 3, 2].
It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.
 

Constraints:

1 <= nums.length <= 1500
1 <= nums[i] <= 105
"""
class Solution:
    """
    BruteForce:
    Nested for loop. As the second for loop expand, the subarray under consideration expands
    with it. No need to again travers i to j via another for loop
    """
    def longestBalancedd(self, nums: List[int]) -> int:
        n = len(nums)
        max_subarray_len = 0
        for i in range(n):
            seen_even, seen_odd = set(), set()
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    seen_even.add(nums[j])
                else:
                    seen_odd.add(nums[j])
                if len(seen_odd) == len(seen_even):
                    max_subarray_len = max(max_subarray_len, j-i+1)
        return max_subarray_len
