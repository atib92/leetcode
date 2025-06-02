"""
 Sum of Largest Prime Substrings
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, find the sum of the 3 largest unique prime numbers that can be formed using any of its substrings.

Return the sum of the three largest unique prime numbers that can be formed. If fewer than three exist, return the sum of all available primes. If no prime numbers can be formed, return 0.

Note: Each prime number should be counted only once, even if it appears in multiple substrings. Additionally, when converting a substring to an integer, any leading zeros are ignored.

 

Example 1:

Input: s = "12234"

Output: 1469

Explanation:

The unique prime numbers formed from the substrings of "12234" are 2, 3, 23, 223, and 1223.
The 3 largest primes are 1223, 223, and 23. Their sum is 1469.
Example 2:

Input: s = "111"

Output: 11

Explanation:

The unique prime number formed from the substrings of "111" is 11.
Since there is only one prime number, the sum is 11.
 

Constraints:

1 <= s.length <= 10
s consists of only digits.
"""
import heapq

class Solution:
    def _is_prime(self, substring: str) -> bool:
        num = self._to_int(substring)
        return self.is_prime(num)
    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True  # 2 and 3 are prime

        if n % 2 == 0 or n % 3 == 0:
            return False  # Eliminate multiples of 2 and 3 early

        # Only check odd numbers starting from 5 up to sqrt(n)
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6  # Check 6k ± 1 pattern

        return True

    def _to_int(self, substring: str) -> int:
        return int(substring)
    def sumOfLargestPrimes(self, s: str) -> int:
        """
        Find all substrings greedily:
        l = 0, r = N-1 to 1
        l = 1, r = N-1 to 1
        ...
        For substrings that are prime, save until you have 3 or no more substring can be formed
        Use min heap so that the minimum can easily be deleted if the heap become larger than 3
        """
        topKprime = []
        N = len(s)
        for l in range(N):
            r = N-1
            while(r >= l):
                substring = s[l:r+1]
                if self._is_prime(substring):
                    elem = self._to_int(substring)
                    if elem not in topKprime:
                        heapq.heappush(topKprime, elem)
                        if len(topKprime) > 3:
                            while(len(topKprime) > 3):
                                heapq.heappop(topKprime)
                r -= 1
        return sum(topKprime)
