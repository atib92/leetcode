"""
LINKEDIN SCREENING ROUND QUESTION
Given an array arr. Find the sum of all subarrays of the array since the sum could be very large print the sum modulo (109+7).

Examples:

Input: arr[] = [1, 2, 3]
Output: 20
Explanation: All subarray sums are: [1] = 1, [2] = 2, [3] = 3, [1,2] = 3, [2,3] = 5, [1,2,3] = 6. Thus total sum is 1+2+3+3+5+6 = 20.
Input: arr[] = [1, 3]
Output: 8
Explanation: All subarray sums are: [1] = 1 [3] = 3 [1,3] = 4. Thus total sum is 1+3+4 = 8.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints :
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 109
"""
class Solution:
    def subarraySum(self, arr):
        """
        [1 2 3]
        
        sub arrays starting at 1
        [1] [1 2] [1 2 3]
        arr[0]*N + arr[1]*N-1 + ... + arr[N-1]*1
        
        sub arrays starting at 2
        [2] [2 3]
                   arr[1]*N-1 + .... + arr[N-1]*1
        
        sub arrays starting at 3
        [3]
                               arr[2]*N-1 + ...+
        Total :
        arr[0] * N
        arr[1] * 2(N-1)
        arr[2] * 3(N-2)
        Time O(N) Space O(1)
        """
        sum = 0
        N = len(arr)
        for index, num in enumerate(arr):
            sum += num * (index+1) * (N-index)
        return sum % (pow(10,9) + 7)
