"""
 Find K Closest Elements
Solved
Medium
Topics
conpanies icon
Companies
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]

 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""

class Solution:
    """
    Step 1: Find the lower bound index. This is the smallest element in arr that is greater than equal to the target value.
    Step 2: Start from lower_bound - 1, lower_bound and use this to compose a window of k elements. 
    """
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        def search(arr, x):
            l, r = 0, n-1
            while(l < r):
                m = (l+r)//2
                if arr[m] == x:
                    return m
                elif arr[m] > x:
                    r = m
                else:
                    l = m+1
            return l
        R = search(arr, x)
        L = R-1
        out = []
        while(k > 0):
            if L < 0 and R > n-1:
                return []
            elif L >= 0 and R <= n-1:
                if abs(arr[L]-x) <= abs(arr[R]-x):
                    L -= 1
                else:
                    R += 1
            elif L >= 0:
                L -= 1
            else:
                R += 1
            k -= 1
        return arr[L+1:R]
