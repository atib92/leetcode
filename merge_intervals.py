"""
Merge Intervals
Solved
Medium
Topics
conpanies icon
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Algorithm: Denote the current interval as a (start, end) tuple and traverse the input to merge intervals
        if the end of the currrent interval is >= start of the next interval.
        Note: For case where the end of the current interval > end of next interval, the current end is to be
        continued for the running open interval.
        """
        # Sort based on interval start
        intervals = sorted(intervals, key=lambda x: x[0])
        N = len(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        i = 0
        out = []
        while(i < N):
            while(i < N-1 and end >= intervals[i+1][0]):
                i += 1
                end = max(end, intervals[i][1])
            out.append([start, end])
            if i < N-1:
                # We exited because of the second condition, there are more intervals to process so start from the next interval
                i += 1
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                # Nothing to process so we can end. Just increment i to get out of the loop
                i += 1
        return out
