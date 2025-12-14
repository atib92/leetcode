"""
 Minimum Operations to Make Binary Palindrome
Solved
Medium
Topics
Hint
You are given an integer array nums.

For each element nums[i], you may perform the following operations any number of times (including zero):

Increase nums[i] by 1, or
Decrease nums[i] by 1.
A number is called a binary palindrome if its binary representation without leading zeros reads the same forward and backward.

Your task is to return an integer array ans, where ans[i] represents the minimum number of operations required to convert nums[i] into a binary palindrome.

 

Example 1:

Input: nums = [1,2,4]

Output: [0,1,1]

Constraints:

1 <= nums.length <= 5000
​​​​​​​1 <= nums[i] <= 5000

"""
from functools import cache

@cache
def _to_binary(num):
    out = []
    while num:
        out.append(num % 2)
        num //= 2
    return out

@cache
def is_binary_palindrome(num):
    binary = _to_binary(num) # Actually the reversed but works for our use case :-) 
    return binary == binary[::-1]

palindromes = [i for i in range(5001) if is_binary_palindrome(i)]
L, R = 0, len(palindromes)-1

class Solution:
    """
    We do a one time setup and find all nums from 0-5000 (check problem constraints) with palindromic binary representations.
    This would generally be in __init__ but to make it common across all test cases in LeetCode we
    put the setup at module level. 
    Once the setup is done, the problem boils down to finding the closeset number in the above list
    from a the input given number. We use binary search for that.
    """
    def distance(self, num):
        l, r = L, R
        while(l < r):
            m = (l + r) // 2
            if palindromes[m] >= num:
                r = m
            else:
                l = m+1
        left, right = l-1, l
        if left >=0 and right >= 0:
            return min(abs(num-palindromes[left]), abs(num-palindromes[right]))
        else:
            return abs(num-palindromes[right])
        
    def minOperations(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.append(self.distance(num))
        return res
