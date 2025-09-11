"""
Minimum Operations to Reduce an Integer to 0
Solved
Medium
Topics
conpanies icon
Companies
Hint
You are given a positive integer n, you can do the following operation any number of times:

Add or subtract a power of 2 from n.
Return the minimum number of operations to make n equal to 0.

A number x is power of 2 if x == 2i where i >= 0.

 

Example 1:

Input: n = 39
Output: 3
Explanation: We can do the following operations:
- Add 20 = 1 to n, so now n = 40.
- Subtract 23 = 8 from n, so now n = 32.
- Subtract 25 = 32 from n, so now n = 0.
It can be shown that 3 is the minimum number of operations we need to make n equal to 0.
Example 2:

Input: n = 54
Output: 3
Explanation: We can do the following operations:
- Add 21 = 2 to n, so now n = 56.
- Add 23 = 8 to n, so now n = 64.
- Subtract 26 = 64 from n, so now n = 0.
So the minimum number of operations is 3.
 

Constraints:

1 <= n <= 105
"""
"""
Transform streak of ones | Bit count | Python | Constant Time

atib
50 Days Badge 2025
0
a few seconds ago
Python3
Intuition
The idea is pretty simply:

Case-A: Everytime you come across a strek of ones e.g: ...??01111000.. you can transform it to ...??10000000.. in ONE step (adding 2^k where k is the bit position of the first one in that streak)
Case-B: Everytime you come across a solo 1 .eg 010, you can remove it in one operation by subtracting 2^k where k is the bit position of the set bit
Approach
Traverse from bit position 0 to 20 (chosen 20 since 2^20 >> max n possible)
maintain a streak of ones
Everytime a streak ends, do the following:
i. If the lenght of the steam is > 1, this is Case-A, set the current bit position (where the streak ended) and increment steps by 1 since we have added 2^(steak starting bit position)
ii. If the lenght of the steak is just 1, we know this is solo 1 so we just need to increment stesp and move on (case-B)
iii. If the lenght of the steak is 0, we continue.
NoteL ii and iii. can be combined via steps += streak (since in case iii the streak length is 0 (NOP) )
Complexity
Time complexity:
O(1) : Just go over 20 bits
Space complexity:
O(1) : Just maintaining a streak and steps variable.
Code
"""
class Solution:
    def minOperations(self, n: int) -> int:
        def is_set(n, i):
            return n & (1 << i) != 0
        """
        max n is 100000 < pow(2,20) so lets considering only 20 bits 
        Algo:
        1. Traverse over the binary representation of n
        2. Detect groups of > 1 consecutive zeros. For each such group:
            a. Increment steps by 1
            b. Reset all the bits from start,end of the group
            c. Set the end+1th bit
        3. For solo zeros, just increment steps for every solo zero
        """
        steps = 0
        streak = 0
        for bit in range(20):
            if is_set(n, bit):
                # continue the streak
                streak += 1
            else:
                # bit is reset
                if streak > 1:
                    # end of a streak
                    steps += 1
                    streak = 1
                else:
                    # either 010... or 000... ie a steak of of size 0 or 1.
                    # if one, its a solo one so count it. (for streak of 0, steps+=streak doesn't do anything)
                    steps += streak
                    streak = 0
        return steps 
