"""
Minimum Domino Rotations For Equal Row
Solved
Medium
Topics
Companies
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 

Example 1:


Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= tops.length <= 2 * 104
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6
"""
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        1. Each face can have 6 values 1-6
        2. Either all tops are going to have same value or all bottoms are going to have same value (from 1-6)
        Algo: We can try out each target (1-6) and compute if possible how many rotations would be needed to make either all tops to target or all bottoms to target
        Optimization: If all tops/bottoms are going to have the same value then the possible target are just really tops[0] or bottoms[0] !!
        Time : O(N)
        """
        N = len(tops)
        min_rotations = 20001
        T = [tops[0], bottoms[0]]
        for target in T:#[1,2,3,4,5,6]:
            rotations = 0
            for pos in range(N):
                if tops[pos] != target:
                    if bottoms[pos] == target:
                        rotations += 1
                    else:
                        break
            if pos == N-1:
                min_rotations = min(min_rotations, rotations)
        for target in T:#[1,2,3,4,5,6]:
            rotations = 0
            for pos in range(N):
                if bottoms[pos] != target:
                    if tops[pos] == target:
                        rotations += 1
                    else:
                        break
            if pos == N-1:
                min_rotations = min(min_rotations, rotations)
        return min_rotations if min_rotations != 20001 else -1



"""
Cleaner code with less duplication.
"""
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def make_all_tops_same(tops, bottoms):
            n = len(tops)
            min_rotations = float("inf")
            for target in range(1, 7):
                rotations = 0
                skip = False
                for index in range(n):
                    if tops[index] == target:
                        continue
                    elif bottoms[index] == target:
                        rotations += 1
                    else:
                        skip = True
                        break
                if skip == False:
                    # We have been able to make all tops equal to target
                    min_rotations = min(rotations, min_rotations)
            return min_rotations
        rotations = min(make_all_tops_same(tops, bottoms), make_all_tops_same(bottoms, tops))
        if rotations == float("inf"):
            return -1
        return rotations
