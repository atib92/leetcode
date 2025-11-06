"""
Bulb Switcher
Solved
Medium
Topics
conpanies icon
Companies
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

 

Example 1:


Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 1

"""
from math import sqrt
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))


"""
Wait, what the **** just happened ?
Realisation 1:
If you lay down what bulbs are affected in any iteration, you would notice the following:
A bulb is toggled in ith iteration only if i is a factor of bulb_# a.k.a the total no. of toggles of the bulb = number of factors.
So only bulbs with ODD number of toggles will remains ON at the end i,e only bulbs that have ODD number of factors.
Realisation 2:
Only perfect squares have ODD number of factor since factors come in pairs. Total # of factors are ODD only if there are repeats. eg: 9 - (1,3,3)
Realisation 3:
So we just count the number of perfect squars <= n
Realisation 4:
If you just compute the floor of sqrt(n) all number from 1 to that number will have squars <= 100 so the answer is just sqrt(n)

Complexity: sqrt(n) but O(1) since most languages uses an optimised inverse square root technique to compute the square root in constant time.
"""
