"""
Single Number III
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
 

Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""
class Solution:
    def singleNumber_I(self, nums: List[int]) -> List[int]:
        """
        Lets use python set for quick lookup
        Time: O(N)
        Space: O(N)
        A O(1) space approach can be thought of via some fancy XOR'ing next !!.
        """
        out = set()
        for num in nums:
            if num in out:
                out.remove(num)
            else:
                out.add(num)
        return list(out)
    
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        If we do a cumulative XOR of all numbers: cum_xor = a xor b
        where a and b are the two numbers which occur only once. Now,
        can we use cum_xor to find a and b ?

        We analyse the bits of cum_xor, say the ith bit is SET i,e
        either ith bit is:
        i.  SET in a and RESET in b   
                    OR
        ii. RESET in a and SET in b
        if we use this ith bit to group nums in two different groups, we
        are sure that a and b will in different groups. All other numbers
        would fall in one group or other. Whichever group these other
        numbers get classified in, they will be in pairs so if we do a cum_xor
        of the groups we will end up with a and b.
        """
        cum_xor = 0
        for num in nums:
            cum_xor ^= num
        i = 0
        for bit in range(33):
            # Detect a bit that is SET
            if cum_xor % 2 == 0:
                i += 1
                cum_xor = cum_xor // 2
            else:
                break
        # bit # i is set, use this to groups nums
        group1 = []
        group2 = []
        for num in nums:
            if num & (1 << i) != 0:
                group1.append(num)
            else:
                group2.append(num)
        out = []
        # Hence forth this a problem of finding the single # in a list where
        # all other numbers occur in pairs.
        # TODO: Move this to a util !
        g_xor = 0
        for num in group1:
            g_xor ^= num
        out.append(g_xor)
        g_xor = 0
        for num in group2:
            g_xor ^= num
        out.append(g_xor)
        return out
