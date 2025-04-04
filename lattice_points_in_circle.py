"""
Source: https://leetcode.com/problems/count-lattice-points-inside-a-circle/description/ 
Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith circle drawn on a grid, return the number of lattice points that are present inside at least one circle.
Note:
A lattice point is a point with integer coordinates.
Points that lie on the circumference of a circle are also considered to be inside it.
"""

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        """
        Simple Euclidean distance formula. Starting from 0,1...diamter try out all coordinates in any circle
        and save the points in a set for de-duplication.
        """
        points = set()
        for circle in circles:
            # x: circle[0] y: circle[1] r:circle[2]
            for x in range(-circle[2], circle[2]+1):
                for y in range(-circle[2], circle[2]+1):
                    if pow(x,2) + pow(y,2) <= pow(circle[2],2):
                        points.add(f'{x+circle[0]}:{y+circle[1]}')
        return len(points)
