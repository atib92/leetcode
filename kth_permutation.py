"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!
"""
class Solution:
    @cache
    def fact(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n*self.fact(n-1)
    def _getPermutation(self, prefix, nums, k):
        """
        The crux of this problem is understading the optimal substructure of the problem. Given n numbers, there are n! permuations,
        the n! permuations can be divided in n groups of each (n-1)! combinations. At any step you need to narrow down the problem
        by finding which group out of the n the kth permuation is likely to be found and what the index (k') of the particular permuation
        in the next group.

        ** NEXT LEVEL : Please refer kth_permutation.py for when the string has duplicates. **
        """
        if k == 0:
            return prefix + "".join(nums)
        else:
            n = len(nums)
            group = k // self.fact(n-1) # --> group of index. 
            k = k % self.fact(n-1)      # --> kth element of that group
            pivot = nums[group]         # --> group i starts with nums[i] followd by the other numbers
            prefix += pivot
            nums.remove(pivot)
            return self._getPermutation(prefix, nums, k)
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i+1) for i in range(n)]
        k = k - 1 # O based indexing
        return self._getPermutation("", nums, k)
        
