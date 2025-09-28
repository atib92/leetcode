"""
A nephew found out that his uncle loves him so much that he would do anything to buy him as many gifts as he possibly can.
For this reason, the nephew prepares a list of gifts that he wants and gives it to his uncle.
Each item in the list contains 2 integers: the day on which he wants the gift (today is day 0), and the cost of it.
The uncle, knowing that his nephew is preparing such a list, saves $1 per day for the gifts, and initially (on day 0) he has $0.
Calculate the maximum number of gifts the uncle can buy to his nephew.
"""

"""
Family of greedy problem: Try buying all gifts if possible, the moment you overprovision
that is current_expenditure > available_money, you remove the worst past decision which
in this case is the most expensive gift bought so far. MAX HEAP is your friend. Also see
furthest_building_you_can_reach.py for a similar problem.
"""

import heapq
from typing import List, Tuple

def max_gifts(gifts: List[Tuple[int, int]]) -> int:
    """
    gifts: list of (day, cost)
    returns: maximum number of gifts purchasable
    """
    # sort by day
    gifts.sort(key=lambda x: x[0])
    # use a max-heap: Python's heapq is min-heap, so store negative costs
    max_heap = []  # store negative costs
    total = 0

    for day, cost in gifts:
        heapq.heappush(max_heap, -cost)
        total += cost
        # if total money spent exceeds money available by this day, drop most expensive/wasteful chosen gift
        if total > day:
            most_expensive = -heapq.heappop(max_heap)
            total -= most_expensive

    return len(max_heap)




# Example
gifts = [(5,5), (6,3), (7,3)]
#gifts = [(11,8),(12,4),(13,3),(14,5)]
gifts = [(5,3), (6,5), (7,3)]
print(max_gifts(gifts))  # prints maximum number of gifts

"""
gifts = [(5,5), (6,3), (7,3)]

heap: 5
c = 5 d = 5

heap 5
    /
   3

c = 8, d = 6 c > d so we need to remove a gift, we greedily remove the costliest gift
heap 3
c = 3 d = 6

    3
  /
3
c = 6 d = 6 
Ans: 2


[(5,3), (6,5), (7,3)]
h = 3
c = 3
d = 5

h = 5
   /
  3

c = 8
d = 6
c > d so remove the costliest

h = 3
c = 3
d = 6


h = 3
   /
  3
c = 6
d = 6 --> ans = 2
"""
