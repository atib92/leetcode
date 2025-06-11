"""
Find the Prefix Common Array of Two Arrays
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

 

Example 1:

Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
Example 2:

Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
 

Constraints:

1 <= A.length == B.length == n <= 50
1 <= A[i], B[i] <= n
It is guaranteed that A and B are both a permutation of n integers.
"""
class Solution:
    def findThePrefixCommonArray_Nsquare(self, A: List[int], B: List[int]) -> List[int]:
        """
        Time: O(N^2)
        Space: O(N)
        Add elements from A and B to their resp. sets and at all index, compute the count of the interesection set.
        """
        freqA = set()
        freqB = set()
        N = len(A)
        out = [0] * N
        for i in range(N):
            freqA.add(A[i])
            freqB.add(B[i])
            out[i] = len(set.intersection(freqA, freqB))
        return out
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        Rather than computing the intersection at each index, we simply track the presence / absence of n in arr[51].
        At any index, if A[i] and B[i] are s.t that add one to the common set, we increment the count.
        Time: O(N)
        """
        arrA = [False] * 51
        arrB = [False] * 51
        N = len(A)
        out = [0] * N
        last = 0
        for i in range(N):
            a = A[i]
            b = B[i]
            if a == b and arrA[a] is False and arrB[a] is False:
                last += 1
            else:
                # Case1: a not in A till now but a in B already: last += 1
                if arrA[a] is False and (arrB[a] is True):
                    last += 1
                # Case2: b not in B till now but b in A already: last += 1
                if arrB[b] is False and (arrA[b] is True):
                    last += 1
            arrA[a] = True
            arrB[b] = True
            out[i] = last
        return out
