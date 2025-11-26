"""
Two City Scheduling
Solved
Medium
Topics
conpanies icon
Companies
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

 

Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
Example 2:

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
Example 3:

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086
"""
import heapq

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Allocate cost to city_one
        if the allocation become greater than n, move the best 
        cost to city_two. Track best cost via min heap
        Evey time (a, b) is allocated to city_one, we have avoided cost_b-cost_a.
        We incur that cost when we move that allocation to city_two.
        """
        heap = []
        n = len(costs) // 2
        count = 0
        total = 0
        for cost_one, cost_two in costs:
            count += 1
            total += cost_one
            heapq.heappush(heap, -cost_one+cost_two)
            if count > n and heap:
                count -= 1
                total += heapq.heappop(heap)
        return total
