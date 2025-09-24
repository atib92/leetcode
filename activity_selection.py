"""
Given two arrays start[] and finish[], representing the start and finish times of activities. A person can perform only one activity at a time, and an activity can be performed only if its start time is greater than the finish time of the last chosen activity.
Find the maximum number of activities that can be performed without overlapping.

Examples:  

Input: start[] = [1, 3, 0, 5, 8, 5], finish[] = [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: A person can perform at most four activities. The maximum set of activities that can be performed is {0, 1, 3, 4} (these are the indexes in the start[] and finish[] arrays).

Input: start[] = [10, 12, 20], finish[] = [20, 25, 30]
Output: 1
Explanation: A person can perform at most one activity.
"""

"""
The standard greey approach is to sort by endtime so we naturally pick those events first that ends first.
I tried "select by start time" and it worked for all test cases. The extra manual step here is propagate
the minimum end time forward on conflict.
"""

class Solution:
    def activitySelection_SortByStartTime(self, start, finish):
        #code here
        count = 0
        events = zip(start, finish)
        events = sorted(events, key=lambda x: x[0])
        prev_end_time = -1
        for start_time, end_time in events:
          if start_time > prev_end_time:
            count += 1
            prev_end_time = end_time
          else:
            # Greedy
            prev_end_time = min(end_time, prev_end_time)
        return count
        
    def activitySelection(self, start, finish):
        #code here
        count = 0
        events = zip(start, finish)
        events = sorted(events, key=lambda x: x[1])
        prev_end_time = -1
        for start_time, end_time in events:
          if start_time > prev_end_time:
            count += 1
            prev_end_time = end_time
            # Since we have already sorte by end time we know, on conflict the minimum (prev) endtime is natually propagated further
        return count
