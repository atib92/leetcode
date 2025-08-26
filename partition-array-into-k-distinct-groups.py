"""
 Partition Array Into K-Distinct Groups
Solved
Medium
conpanies icon
Companies
Hint
You are given an integer array nums and an integer k.

Your task is to determine whether it is possible to partition all elements of nums into one or more groups such that:

Each group contains exactly k distinct elements.
Each element in nums must be assigned to exactly one group.
Return true if such a partition is possible, otherwise return false.

 

Example 1:

Input: nums = [1,2,3,4], k = 2

Output: true

Explanation:

One possible partition is to have 2 groups:

Group 1: [1, 2]
Group 2: [3, 4]
Each group contains k = 2 distinct elements, and all elements are used exactly once.

Example 2:

Input: nums = [3,5,2,2], k = 2

Output: true

Explanation:

One possible partition is to have 2 groups:

Group 1: [2, 3]
Group 2: [2, 5]
Each group contains k = 2 distinct elements, and all elements are used exactly once.

Example 3:

Input: nums = [1,5,2,3], k = 3

Output: false

Explanation:

We cannot form groups of k = 3 distinct elements using all values exactly once.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
​​​​​​​1 <= k <= nums.length
"""
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        L = len(nums)
        """
        For L to be divided in groups of exact k elements, L shd be divisibe by k
        but each group must contain only distinct elements, element might be duplicated
        across groups (differnet indexes in nums)
        """         
        if L % k != 0:
            # early exit if L is not a multiple of k
            return False
        else:
            num_groups = L // k
            """
            1. We are now sure that nums can be distributed in num_groups of k each.
            2. We just need to make sure that no group has duplicate elements. For
               that we can frequency count each num in nums and ensure no num appears
               > num_groups times
            """
            frequency = {}
            for num in nums:
                count = frequency.get(num, 0)
                count += 1
                if count > num_groups:
                    return False
                frequency[num] = count
            return True
