"""
 Count Bowl Subarrays
Solved
Medium
Topics
conpanies icon
Companies
Hint
You are given an integer array nums with distinct elements.

A subarray nums[l...r] of nums is called a bowl if:

The subarray has length at least 3. That is, r - l + 1 >= 3.
The minimum of its two ends is strictly greater than the maximum of all elements in between. That is, min(nums[l], nums[r]) > max(nums[l + 1], ..., nums[r - 1]).
Return the number of bowl subarrays in nums.

 

Example 1:

Input: nums = [2,5,3,1,4]

Output: 2

Explanation:

The bowl subarrays are [3, 1, 4] and [5, 3, 1, 4].

[3, 1, 4] is a bowl because min(3, 4) = 3 > max(1) = 1.
[5, 3, 1, 4] is a bowl because min(5, 4) = 4 > max(3, 1) = 3.
Example 2:

Input: nums = [5,1,2,3,4]

Output: 3

Explanation:

The bowl subarrays are [5, 1, 2], [5, 1, 2, 3] and [5, 1, 2, 3, 4].

Example 3:

Input: nums = [1000000000,999999999,999999998]

Output: 0

Explanation:

No subarray is a bowl.

 

Constraints:

3 <= nums.length <= 105
1 <= nums[i] <= 109
nums consists of distinct elements.
"""


"""
Algorithm:
[2,5,3,1,4]
A valid bowl looks like a valley ie two large values and all smaller values in between.
For any index to be a starting point of a bowl, we need to find the immediate next larger element.
So this essentially boils to next largest computation which can be done via a monotonic stack.
* if TOS is a larger value, we push the current elem
* if TOS is a smaller value, we have a potential bowls between TOS and current elem.
* As long as TOS < current elem, we keep on popping and check if the bowl is valid
* Finally when we push the current elem, its definitely less than TOS. We also know all the intermediate elements (that got popped) we
  smaller than the current element ,so we have a new potential bowl between TOS......Current elem, check if this bowl is valid and increment count.
* Finally push the current element to the stack
"""

class Solution:        
    def bowlSubarrays(self, arr: List[int]) -> int:
        s = []
        res = 0
        for index, elem in enumerate(arr):
            # Every [popped index,index] subarray is a potential bowl. Check if its valid bowl (len >= 3)
            while s and elem >= arr[s[-1]]:
                popped_index = s.pop()
                if index >= popped_index + 2:
                    res += 1
            # Now the stack is sure decreasing. LARGE_LAST_TOS ..SMALL_CURRENT_ELEMENT_NOW
            # All the elements in between that were popped were < SMALL_CURRENT_ELEMENT_NOW
            # So this fits the definition of a bowl. Again just check its valid
            if s and index - s[-1] >= 2:
                res += 1
            s.append(index)
        return res

        
