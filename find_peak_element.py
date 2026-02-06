'''
Find Peak Element
Solved
Medium
Topics
conpanies icon
Companies
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        The key observation here is that given the constraint that no two adjacent elements are going to be same gurantees
        there will always be a peak in the array. With that observation, we can use binary search as follows:
        if mid elem < mid + 1 elem : We are guranteed to see a peak in the right [mid+1:...] so move l to mid+1
        if mid elem > mid + 1 elem : We are guranteed to see a peak in the left [:mid] (note: including mid elem)
        Note: moving to either left or right side of the array gurantees to see atleast one peak on that side. Its not saying
        the same as that a peak cannot be seen on the other side. 
        '''
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] > nums[mid + 1]:
                # guranteed to see a peak on the right
                r = mid
                # why not mid - 1 ? Since mid might be the peak !
            else:
                # guranteed to see a peak on the left
                l = mid + 1
                # why not mid ? since mid can never be the peak
        return l # l is now equal to r, return either.
    

