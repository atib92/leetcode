"""
Source : https://leetcode.com/problems/container-with-most-water/description/
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

class Solution:
    """
    The idea is to start with the container between [0, N]. This has an area of min(arr[N],arr[0])*(N-0)
    Now we need to move l, r such that we can try other start and end points of the container. We need to
    move such that there is possibility of getting a bigger container. Obviously that happens only if we
    move the pointer with the lower height value and retaining the pointer with the higher height value
    since that keeps the possibilty of getting higher hieghts later and hence potentially more water/area
    container.
    Time: O(N)
    Space: O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        l, r, _max = 0, len(height)-1, 0
        while(l < r):
            delta = r - l 
            if height[l] <= height[r]:
                _max = max(_max, delta * height[l])
                l += 1
            else:
                _max = max(_max, delta * height[r])
                r -= 1
        return _max
