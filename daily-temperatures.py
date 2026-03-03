'''
Daily Temperatures
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Montonic Decreasing Stack based algorithm
        Push indexes
        Step by Step:
        [73,74,75,71,69,72,76,73,INF]
         0  1  2  3  4  5  6  7  8
         index 0: stack [0]
         index 1: Pop 0 and set out[0] = 1 stack [1]
         index 2: Pop 1 and set out[1] = 1 stack [2]
         index 3: stack [2 3]
         index 4: stack [2 3 4]
         index 5: ... 
        '''
        stack = []
        n = len(temperatures)
        out = [0] * n
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                pop_index = stack.pop()
                out[pop_index] = i - pop_index
            stack.append(i)
        return out
