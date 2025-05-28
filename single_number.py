"""
Single Number II
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
"""
class Solution:
    def singleNumber_bruteforce(self, nums: List[int]) -> int:
        """
        Time Complexity : O(n^2)
        Space Complexity : O(n)
        """
        for i, n in enumerate(nums):
            if n not in nums[:i] and n not in nums[i+1:]:
                return n
    def singleNumber(self, nums: List[int]) -> int:
        """
        Linear/Optimal Algo: Count the number of bits in every position. All bit counts except for the ones contributed by the
        number that occurs only once will be a multiple of 3. We recreate the odd number using that piece of info. 
        Note: For -ve numbers, you can store the count of -ve number or the -ve bit in bits[32]. I have done the former.
        """
        neg = 0
        bits = [0] * 32 # For 32 bits
        for n in nums:
            if n < 0:
                neg += 1 # You could do bits[31] += 1 here and later if bits[31] % 3 != 0, sign = -1
            n = abs(n)
            pos = 0
            while(n != 0):
                if n % 2 == 1:
                    bits[pos] += 1
                pos += 1
                n = n // 2
        ans = 0
        for index, bit in enumerate(bits):
            if bit % 3 != 0:
                ans += pow(2,index)
        if neg % 3 != 0:
            sign = -1
        else:
            sign = +1
        return ans*sign
        
