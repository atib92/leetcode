"""
Furthest Building You Can Reach
Solved
Medium
Topics
conpanies icon
Companies
Hint
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

 

Example 1:


Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7
Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3
 

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length
"""
"""
This is typical greedy problem like Uncle->Nephew Gift. The idea in such problem is to overprovision and then greedily fix the worst choice.
To get the worst past choice, a priority queue is typically used
"""


import heapq

class Solution:
    """
        Observation:
        1. A brick can help jump multiple times
        2. A ladder can help jump any height

        Greedy: 
        Use ladder to jump maximum heights so far. At any time there isn't enough
        ladders, swap the last most wasteful usage of ladder with bricks. Most wasteful
        ladder usage is a ladder used to jump minimum height (MIN HEAP)

        Alternative:
        Save ladder to jump larger heights later and exhaust bricks first. When you run
        out of bricks wap the most wasteful bricks usage with a ladder Most wasteful
        bricks usage is a jump that used most number of bricks (MAX HEAP)
        
    """
    def furthestBuildingWorking(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        pos = 0
        pq = []
        while(pos < n):
            if pos == n-1:
                break
            else:
                jump = heights[pos+1]-heights[pos]
                if jump > 0:
                    heapq.heappush(pq, jump)
                    if len(pq) > ladders:
                        bricks -= heapq.heappop(pq)
                        if bricks < 0:
                            return pos
            pos += 1
        return n-1

    def furthestBuildingMaxHeap(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        pos = 0
        pq = []
        while(pos < n):
            if pos == n-1:
                break
            else:
                jump = heights[pos+1]-heights[pos]
                if jump > 0:
                    heapq.heappush(pq, -1*jump)
                    bricks -= jump
                    if bricks < 0:
                        ladders -= 1
                        # Reclaim most wasteful bricks usage
                        bricks += (-1*heapq.heappop(pq))
                    if ladders < 0:
                        return pos
            pos += 1
        return n-1
