"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""

"""
Approach: 
We can try to eat only 1 banana per hour and that gives the max hours it will take to eat all bananas
We can try eating the max pile size of bananas per hour and that gives the min hours it will take to eat all bananas
We do binary search between those two extremes to find the minimum eating rate 

Note: To understand how l, r are chaning in the binary search think along these lines:
At the mid point m, if the # of hours needed to eat all bananas is > h, we need to try try from m+1 onward (m is too slow) a.k.a l = m+1
At the mid point m, if the # of hours needed to eat all bananas is <=h, we can try eating slower than or equal to m, a.k.a r = m
"""



from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cost(k):
            c = 0
            for pile in piles:
                c += ceil(pile / k)
            return c
        l, r = 1, max(piles)
        #if cost(r) > h:
        #    return -1
        while(l < r):
            m = (l+r) // 2
            if cost(m) > h:
                # MUST EAT faster than m
                l = m+1
            elif cost(m) <= h:
                # CAN TRY eating slower than equal to m
                r = m
        return l
