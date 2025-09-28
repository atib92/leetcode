"""
Distinct Points Reachable After Substring Removal
Solved
Medium
Hint
You are given a string s consisting of characters 'U', 'D', 'L', and 'R', representing moves on an infinite 2D Cartesian grid.

'U': Move from (x, y) to (x, y + 1).
'D': Move from (x, y) to (x, y - 1).
'L': Move from (x, y) to (x - 1, y).
'R': Move from (x, y) to (x + 1, y).
You are also given a positive integer k.

You must choose and remove exactly one contiguous substring of length k from s. Then, start from coordinate (0, 0) and perform the remaining moves in order.

Return an integer denoting the number of distinct final coordinates reachable.

 

Example 1:

Input: s = "LUL", k = 1

Output: 2

Explanation:

After removing a substring of length 1, s can be "UL", "LL" or "LU". Following these moves, the final coordinates will be (-1, 1), (-2, 0) and (-1, 1) respectively. There are two distinct points (-1, 1) and (-2, 0) so the answer is 2.

Example 2:

Input: s = "UDLR", k = 4

Output: 1

Explanation:

After removing a substring of length 4, s can only be the empty string. The final coordinates will be (0, 0). There is only one distinct point (0, 0) so the answer is 1.

Example 3:

Input: s = "UU", k = 1

Output: 1

Explanation:

After removing a substring of length 1, s becomes "U", which always ends at (0, 1), so there is only one distinct final coordinate.

 

Constraints:

1 <= s.length <= 105
s consists of only 'U', 'D', 'L', and 'R'.
1 <= k <= s.length
"""

"""
Intuition
The key observation is that the destination is only a function of cumulative change along X and Y Axes.

Approach
Create a sliding window of first k elements (index l=0 to r=k-1). Ignore all the elements in the window and compute the cumulative changes along X and Y Axes. Subsequently keep shifting the window to the right, every shift pushes 'l-1' out of the window and shifts 'r'. Everytime a char enters/exits the window, change the cumulative value (destination cell) by removing/adding its effect.

Complexity
Time complexity:
O(N)
Space complexity:
O(1)
Code
"""
class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        seen = set()
        x, y, n = 0, 0, len(s)
        delta = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
        for i in range(k, n):
            dx, dy = delta[s[i]]
            x,y = x+dx, y+dy
        seen.add((x,y))
        l, r = 1, k
        while(r < n):
            # Add the effect of 'l-1'
            dx, dy = delta[s[l-1]]
            x,y = x+dx, y+dy
            # Remove the effect of 'r'
            dx, dy = delta[s[r]]
            x,y = x-dx, y-dy
            seen.add((x,y))
            l += 1
            r += 1
        return len(seen)

