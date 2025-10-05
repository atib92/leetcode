## EDIT: check largest-rectangle-in-histogram.py for a simpler implementation. The idea is same, to keep a monotonic increasing stack but unlike this implementation
# we can solve the problem by just pushing indexes (and not elements) onto the stack.

"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
"""
class Solution:
    """
    Algo: 
    1. Push (index, elem) if elem >= top of stack (tos). This means we are starting a new rectangle which the older rectangles can continue since they had a smaller height.
    2. Keep on popping (old_index, old_elem) if elem < tos, since you cannot continue older rectangles anymore. On every pop, compute the area of the completed rect. as follows:
       a. area = old_elem * (index - old_index)
       b. max = max(max_so_far, area)
       ... more pops ...
       c. Finally : Push (old_index, elem) : 
       Note: Why are we pushing the array[index] = elem with old_index ?
       Since we have only completed and removed rectagles that has a height > elem but you could still have a rectangle starting at old_index and with a height of elem.
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #[(0, heights[0])] # elem is a tuple (index, height)
        _max = 0
        heights.append(0) # This artificially inserted so that all running rectangles can be popped !
        for index in range(len(heights)):
            if not stack or heights[index] >= stack[-1][1]:
                # could be starting a new rectagle
                stack.append((index,heights[index]))
            else:
                # stop all the rectagles 
                while(stack and stack[-1][1] > heights[index]):
                    pos, val = stack.pop()
                    _max = max(_max, val*(index-pos))
                stack.append((pos,heights[index]))
        return _max
