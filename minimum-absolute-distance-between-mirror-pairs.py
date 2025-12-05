"""
 Minimum Absolute Distance Between Mirror Pairs
Solved
Medium
Topics
Hint
You are given an integer array nums.

A mirror pair is a pair of indices (i, j) such that:

0 <= i < j < nums.length, and
reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed by reversing the digits of x. Leading zeros are omitted after reversing, for example reverse(120) = 21.
Return the minimum absolute distance between the indices of any mirror pair. The absolute distance between indices i and j is abs(i - j).

If no mirror pair exists, return -1.

 

Example 1:

Input: nums = [12,21,45,33,54]

Output: 1

Explanation:

The mirror pairs are:

(0, 1) since reverse(nums[0]) = reverse(12) = 21 = nums[1], giving an absolute distance abs(0 - 1) = 1.
(2, 4) since reverse(nums[2]) = reverse(45) = 54 = nums[4], giving an absolute distance abs(2 - 4) = 2.
The minimum absolute distance among all pairs is 1.

Example 2:

Input: nums = [120,21]

Output: 1

Explanation:

There is only one mirror pair (0, 1) since reverse(nums[0]) = reverse(120) = 21 = nums[1].

The minimum absolute distance is 1.

Example 3:

Input: nums = [21,120]

Output: -1

Explanation:

There are no mirror pairs in the array.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109​​​​​​​
"""
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(n):
            return int(str(n)[::-1])
        seen = {}
        min_distance = float("inf")
        n = len(nums)
        for index in range(n-1,-1,-1):
            num = nums[index]
            reverse_num = reverse(num)
            if reverse_num in seen:
                min_distance = min(min_distance, abs(index-seen.get(reverse_num)))
            seen[num] = index
        if min_distance == float("inf"):
            return -1
        return min_distance
