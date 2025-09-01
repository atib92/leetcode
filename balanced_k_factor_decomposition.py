"""
Balanced K-Factor Decomposition
Solved
Medium
Hint
Given two integers n and k, split the number n into exactly k positive integers such that the product of these integers is equal to n.

Return any one split in which the maximum difference between any two numbers is minimized. You may return the result in any order.

 

Example 1:

Input: n = 100, k = 2

Output: [10,10]

Explanation:

The split [10, 10] yields 10 * 10 = 100 and a max-min difference of 0, which is minimal.

Example 2:

Input: n = 44, k = 3

Output: [2,2,11]

Explanation:

Split [1, 1, 44] yields a difference of 43
Split [1, 2, 22] yields a difference of 21
Split [1, 4, 11] yields a difference of 10
Split [2, 2, 11] yields a difference of 9
Therefore, [2, 2, 11] is the optimal split with the smallest difference 9.

 

Constraints:

4 <= n <= 105
2 <= k <= 5
k is strictly less than the total number of positive divisors of n.
"""
class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        """
        We use a simple recusive approach. Try to decompose n by recursively calling the function
        for k/div for all the divisors. Everytime we accumulate k factors, we know we have got a 
        bunch of k divisors who prod is n. We process the group and maintain min_max_diff across
        all recursion.
        Note: We cache the results for all divisors of a number since that is required multiple time.
        This caching atleast sped up result by 3X
        n,k -> n', k-1 -> n'', k-2,.....
                                                   (44,3)
                                        /                       \
                                    [2](22,2)                   [11](4,2)
                                    /.     \                    /
                            [2,2](11,1)   [2,11](2,1).   [11,2](2,1)
                            [2,2,11].   [2,11,2].     [11,2,2]
        """
        @cache
        def divisors(n):
            ret = []
            div = 1
            while(div <= n/2):
                if n % div == 0:
                    ret.append(div)
                div += 1
            return ret
        def func(n, k, nums):
            nonlocal out
            nonlocal min_max_diff
            if k == 1:
                # If only one more factor is needed, the only thing we can do is n itself !
                nums.append(n)
                mmax, mmin = max(nums), min(nums)
                if mmax - mmin < min_max_diff:
                    out = nums
                    min_max_diff = mmax - mmin
            else:
                for div in divisors(n):
                    func(n//div, k-1, nums + [div])
        min_max_diff = float("inf")
        out = None # This is the final returned combination
        func(n,k,[])
        return out
