"""
526. Beautiful Arrangement
Solved
Medium
Topics
Companies
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 15
"""

class Solution:
    @cache
    def place(self, num, pos):
        # We can also keep a N*N cache to do this lookup in O(1) manually
        ret =  ((num % pos == 0) or (pos % num == 0))
        return ret
    @cache
    def _countArrangement(self, n, pos, path):
        """
        The idea is simply to use recursion but with caching to minimize redudant computation. You can use a dp matrix or the @cache decorator for that.
        Approach: If there was no constraint, how would you compute all permuations. You would try to place N numbers in the 1st position, N-1 numbers in 
        the 2nd position and so on.. that would give you N! computatios. 
        We do something similar but add the constraint. If can only place numbers in a position which satisfies the given constraint. Plus, we also need
        to avoid adding a number in a later position if it has already been added earlier. Well, for that you could either use a visited array but that
        wont allow me to use the @cache decorator plus would be very memory intesive, so we have used bitmasking to mark if a particular elem has already
        been added in an earlier position.
        """
        if pos > n:
            # If we have reached here means we have been able to fill positions 1 to N.
            return 1
        else:
            ret = 0
            for elem in range(1, n+1):
                # Attempt placing elem in postion pos if  1. elem has not already been added 2. elem follows the constraint
                if ((1 << elem) & path) == 0:
                    if self.place(elem, pos) == True:
                        ret += self._countArrangement(n, pos+1, path | (1 << elem))
            return ret
    def countArrangement(self, n: int) -> int:
        return self._countArrangement(n, 1, 0)
        
