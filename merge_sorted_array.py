"""
Merge Sorted Array
Solved
Easy
Topics
conpanies icon
Companies
Hint
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""
class Solution:
    def merge_extra_space(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Time: O(n+m) Space: O(m) Extra space !
        """
        r1, r2, w = 0, 0, 0
        nums1_copy = copy.deepcopy(nums1)
        while(r1 < m and r2 < n):
            if nums1_copy[r1] <= nums2[r2]:
                nums1[w] = nums1_copy[r1]
                r1 += 1
            else:
                nums1[w] = nums2[r2]
                r2 += 1
            w += 1
        while(r1 < m):
            nums1[w] = nums1_copy[r1]
            r1 += 1
            w += 1
        while(r2 < n):
            nums1[w] = nums2[r2]
            r2 += 1
            w += 1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Time: O(n+m) Space: O(1)
        Optimal Solution: Rather than using extra space, we use the space at the end of nums1. Its possible to do that
        if we start sorting nums in descending order backwards since that we are guranteed no number in nums1 will be
        overwritten since at max only n numbers can be inserted in nums1 from nums2 and nums1 alreasy has n zeros at
        the end.
        """
        r1, r2, w = m-1, n-1, m+n-1
        while(r1 >= 0 and r2 >= 0):
            if nums1[r1] >= nums2[r2]:
                nums1[w] = nums1[r1]
                r1 -= 1
            else:
                nums1[w] = nums2[r2]
                r2 -= 1
            w -= 1
        while(r1 >= 0):
            nums1[w] = nums1[r1]
            r1 -= 1
            w -= 1
        while(r2 >= 0):
            nums1[w] = nums2[r2]
            r2 -= 1
            w -= 1
