"""
Majority Element
Solved
Easy
Topics
conpanies icon
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


#1. O(N) Time and O(N) Space
"""
Maintain a hashmap/frequency counter return once you see a majority element
"""

#2. O(N) Time and O(1) Space
"""
This is the Boyer-Moore Algorithm.
We iterate over the input list and maintain a candidate and candidate count. Whenever we see an elem same as candidate we
increment the count else we decreement the count.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                count = 1
                candidate = num
            elif num == candidate:
                count += 1
            else:
                count -= 1
        #if nums.count(candidate) >= len(nums) // 2:
        #    return candidate
        #else:
        #    return None
        # Since the question gurantees a majority always exists, we don't need to do the above extra check (But do it if majority is not guranteed)
        return candidate
