"""
ou are given an array of positive integers nums, and a positive integer k.

You are allowed to perform an operation once on nums, where in each operation you can remove any non-overlapping prefix and suffix from nums such that nums remains non-empty.

You need to find the x-value of nums, which is the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x when divided by k.

Return an array result of size k where result[x] is the x-value of nums for 0 <= x <= k - 1.

A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.

Note that the prefix and suffix to be chosen for the operation can be empty.

 

Example 1:

Input: nums = [1,2,3,4,5], k = 3

Output: [9,2,4]

Explanation:

For x = 0, the possible operations include all possible ways to remove non-overlapping prefix/suffix that do not remove nums[2] == 3.
For x = 1, the possible operations are:
Remove the empty prefix and the suffix [2, 3, 4, 5]. nums becomes [1].
Remove the prefix [1, 2, 3] and the suffix [5]. nums becomes [4].
For x = 2, the possible operations are:
Remove the empty prefix and the suffix [3, 4, 5]. nums becomes [1, 2].
Remove the prefix [1] and the suffix [3, 4, 5]. nums becomes [2].
Remove the prefix [1, 2, 3] and the empty suffix. nums becomes [4, 5].
Remove the prefix [1, 2, 3, 4] and the empty suffix. nums becomes [5].
Example 2:

Input: nums = [1,2,4,8,16,32], k = 4

Output: [18,1,2,0]

Explanation:

For x = 0, the only operations that do not result in x = 0 are:
Remove the empty prefix and the suffix [4, 8, 16, 32]. nums becomes [1, 2].
Remove the empty prefix and the suffix [2, 4, 8, 16, 32]. nums becomes [1].
Remove the prefix [1] and the suffix [4, 8, 16, 32]. nums becomes [2].
For x = 1, the only possible operation is:
Remove the empty prefix and the suffix [2, 4, 8, 16, 32]. nums becomes [1].
For x = 2, the possible operations are:
Remove the empty prefix and the suffix [4, 8, 16, 32]. nums becomes [1, 2].
Remove the prefix [1] and the suffix [4, 8, 16, 32]. nums becomes [2].
For x = 3, there is no possible way to perform the operation.
Example 3:

Input: nums = [1,1,2,1,1], k = 2

Output: [9,6]

 

Constraints:

1 <= nums[i] <= 109
1 <= nums.length <= 105
1 <= k <= 5
"""

class Solution:
    def resultArray_v1(self, nums: List[int], k: int) -> List[int]:
        """
        Brute Force : We fina out all subarrays from nums[i:j] and keep stores its product in dp[i][j].
        Problems: 
        1. The multiplication result can become huge and cause overflow
        2. Since n can be 10^5, O(N^2) woudl anyways not work at scale.
        HENCE THIS ALGORITHM FAILS TO PASS ALL TEST CASES
        """
        out = [0] * k
        N = len(nums)
        dp = [[1] * N for _ in range(N)]
        for i in range(N):
            for j in range(i, N):
                if j == i:
                    dp[i][i] = nums[i]
                else:
                    dp[i][j] = dp[i][j-1] * nums[j]
                x = dp[i][j] % k
                out[x] += 1
        return out
    def resultArray_v2(self, nums: List[int], k: int) -> List[int]:
        """
        This is also a brute force method. We solve problem #1 above by storing the remainders at dp[i][j].
        We use a formulat to propagate the remainder.
        BUT PROBLEM 2 STAYS SINCE THIS IS STILL O(N^2)
        """
        out = [0] * k
        N = len(nums)
        for i in range(N):
            for j in range(i, N):
                if j == i:
                    x = nums[i] % k
                else:
                    # x = (x*nums[i])%k
                    x = (x * (nums[j] % k)) % k 
                out[x] += 1
        return out
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        """
        This is the OPTIMAL SOLUTION.
        We store a DP table where dp[i] is a 'k' sized array which stores the counts of subarrays ending at index 'i' with the corresponding remaineder,
        example: dp[i][r] is the number of subarrays ending at index 'i' with a remainder of r.

        1. Propagation : When we know the remainder of a prev. step dp[i-1][r] = M, we compute what remaineders all these subarrays will produce when the
           ith value is included (using our remainder propagation formula). Note: But do this only if dp[i-1][r] is non zero that only if there exists a
           subarray ending at i-1 that produces remainder 'r'
        2. We can also start new subarrays at index i and those should also contribute to dp[i][r].
        At every step, we add the value of dp[i][:] to ans array and return that at the end.
        Time: O(N*k)
        Space: O(N*k) for the DP array.
        """
        n = len(nums)
        dp = [[0]*k for _ in range(n)]
        ans = [0]*k
        for i in range(n):
            if i > 0:
                # Continue
                for r in range(k):
                    if dp[i-1][r] != 0:
                        # Only if there were subarrays ending at i-1 with ramainder r
                        new_r = (r * (nums[i] % k)) % k
                        #new_r = (r * nums[i]) % k
                        dp[i][new_r] += dp[i-1][r]
            # New Start
            new_r = nums[i] % k
            dp[i][new_r] += 1
            for r in range(k):
                ans[r] += dp[i][r]
        return ans




