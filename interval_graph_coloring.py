"""
Problem
Given n lectures, each with a start time and a finish time, find a minimum number of
lecture halls to schedule all lectures so that no two occur at the same time in the same
hall.
Example
Given lectures A(1, 3], B(1, 5], C(1, 2], D(4, 6], E(4, 8], F(7, 10], G(7, 11], H(9, 13], I(12, 14], J(12, 15],
an optimal schedule uses 3 halls. It schedules lectures C, D, F, J in the first hall, B, G,
I in the second hall, and A, E, H in the third hall.
We will number the halls by positive integers 1, 2, 3, . . . .
"""


import heapq
from typing import List


def min_halls(lectures: List[tuple[int, int]]) -> int:
    lectures.sort(key=lambda x: x[0])
    pq = []
    max_hall_no = 1
    heapq.heappush(pq, (lectures[0][1], max_hall_no))
    for lecture in lectures[1:]:
        if pq[0][0] <= lecture[0]:
            _, hall = heapq.heappop(pq)
            heapq.heappush(pq, (lecture[1], hall))
        else:
            max_hall_no += 1
            heapq.heappush(pq, (lecture[1], max_hall_no))
    return max_hall_no 


lectures = [(1, 3), (1, 5), (1, 2), (4, 6), (4, 8), (7, 10), (7, 11), (9, 13), (12, 14), (12, 15)]
print(lectures)
print(min_halls(lectures))


"""

You can use the data to print/return which lecture halls were assigned to which
lectures. If you are only interested in the number of halls needed, there is a 
simpler version:

for lecture in lectures:
  if pq and pq[0] <= lecture[0]:
    heapq.heappop()
  heapq.heappush(lecture[1])
return len(pq)


The pop basically removes any lectures which are done and the same hall is to
be used in another lecture. At the end what we are left with in the queue is the
number of distinct halls.

If however you need the tagging of lecture:hall_no, you need to track the hall_no
explicitly as shown in my first implementation

"""
