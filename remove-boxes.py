"""
Remove Boxes
Solved
Hard
Topics
Companies
You are given several boxes with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

Return the maximum points you can get.

 

Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)
Example 2:

Input: boxes = [1,1,1]
Output: 9
Example 3:

Input: boxes = [1]
Output: 1
 

Constraints:

1 <= boxes.length <= 100
1 <= boxes[i] <= 100
"""

from functools import cache


class Solution:
    @cache
    def _removeBoxes(self, start, end, count):
        #print(f'_removeBoxes start: {start} end: {end} count: {count}')
        if start > end:
            return 0
        else:
            while(start < end and self.boxes[start] == self.boxes[start+1]):
                start += 1
                count += 1
            # A
            score = (count+1)*(count+1) + self._removeBoxes(start+1, end, 0)
            # B
            for m in range(start+1, end+1):
                if self.boxes[m] == self.boxes[start]:
                    score = max(score, self._removeBoxes(start+1, m-1, 0) + self._removeBoxes(m, end, count+1))
        return score
    def removeBoxes(self, boxes: List[int]) -> int:
        """
        Dynamic Programming:
        start = 0, end = n-1, count = 0 (the number of elems same as boxes[start] to the left of start)
        move start until boxes[start] != boxes[start+1] and keep on incrementing count
        now start is pointing to the last in the cosecutive stream of numbers and count+1 is the total # of 'start' elements
        E.g [112.......N]
        start = 0, count = 0
        start = 1, count = 1
        Now: we can do the following:
        1. 
            i. We can collect the count+1 number of 'start' elements i,e score = (count+1)^2
            ii. Find the score for boxes[start+1, end] removeBoxes(start+1, end, 0)
            A = i + ii
        2.
            What if there are more elements from start+1 onward till end that is equal to 'start' ?
            Lets say we have a boxes[j] == boxes[start] for start < j <= end, we can get a stream
            of of count+1 numbers if we can remove all elements from start+1 to j-1
            i. removeBoxes(m, end, count+1)
            ii. removeBoxes(start+1, m-1, 0)
            C = i + ii
        return max(A, C)
        Memoization: 
        Save dp[start][end][count] state. Can use python decorator @cache for this
        """
        self.boxes = boxes
        ret = self._removeBoxes(0, len(boxes)-1, 0)
        self._removeBoxes.cache_clear()
        return ret
