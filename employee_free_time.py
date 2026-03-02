'''
Employee Free Time
Solved
Hard
Topics
conpanies icon
Companies
Hint
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
'''
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
from collections import defaultdict
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        '''
        [[[1,2],[5,6]],[[1,3]],[[4,10]]]

        [1,2]       [5,6]
        [1,   3]
                 [4,         10]
        Approach: Line Sweep Algo
        Note: Since the intervals are already sorted, we can use merge intervals approach here and just return gaps.
        '''
        line_sweeper = defaultdict(int)
        for emp_schedule in schedule:
            for interval in emp_schedule:
                line_sweeper[interval.start] += 1
                line_sweeper[interval.end] -= 1
        # Caculator cumulative sum now
        last_sum = 0
        start = None
        out = []
        keys = sorted(line_sweeper.keys())
        for k in keys:
            line_sweeper[k] += last_sum
            last_sum = line_sweeper[k]
            if line_sweeper[k] == 0:
                start = k
            else:
                # not zero
                if start is not None:
                    out.append(Interval(start, k))
                    start = None
        return out

