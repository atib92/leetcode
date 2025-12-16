"""
Search in Rotated Sorted Array
Solved
Medium
Topics
conpanies icon
Companies
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
         0 1 2 3 4 5 6
        [4,5,6,7,0,1,2]
        1. Find the index which is < arr[0], index=4 here. This is the point of rotation / breakpoint
        2. Binary search in arr[:i] or arr[i:] to find the target.
        Optimization: You can compare arr[index] with target and decide to only search in one of the two sub arrays
        """
        def search(l, r, target):
            while(l <= r):
                mid = (l+r) >> 1
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    # search left
                    r = mid - 1
                else:
                    # search right
                    l = mid + 1
            return None
        def find_break_point():
            t = nums[0]
            # find the minimum element < t
            l, r = 1, n-1
            index = n-1
            while(l <= r):
                mid = (l + r) >> 1
                if nums[mid] > t:
                    # search 
                    l = mid + 1
                elif nums[mid] <= t:
                    index = mid
                    r = mid - 1
            return index
        n = len(nums)
        index = find_break_point()
        left_res = search(0, index-1, target)
        if left_res is not None:
            return left_res
        right_res = search(index, n-1, target)
        if right_res is not None:
            return right_res
        return -1

