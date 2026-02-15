'''
Reaching Points
Solved
Hard
Topics
conpanies icon
Companies
Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, or false otherwise.

The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).

 

Example 1:

Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: true
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)
Example 2:

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: false
Example 3:

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: true
 

Constraints:

1 <= sx, sy, tx, ty <= 109
'''
class Solution:
    def reachingPoints_ForwardBruteForce(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        '''
        ONLY FOR DEMONSTRATION
        x,y -> (x, x+y) and (x+y, y)
        1,1 -> (2,1) (1,2)
                (3,1)(2,3)(3,2),(1,3)
                (4,1)(3,4)(5,3)(2,5)(5,2)(3, 5)*
        # Brute Force: Recursion and save a memo table, prune paths if it goes beyond any target dimension
        O(2^N)
        In the forward direction each x,y generates 2 possible next points.
        '''
        memo = {}
        def traverse(sx, sy):
            if sx == tx and sy == ty:
                return True
            else:
                if (sx, sy) in memo:
                    return memo.get((sx,sy))
                else:
                    if sx > tx or sy > ty:
                        ret = False
                    else:
                        ret = traverse(sx+sy, sy) or traverse(sx, sx+sy)
                    memo[(sx,sy)] = ret
                    return memo[(sx, sy)]
        return traverse(sx, sy)
    
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        '''
        Observation-1
        If we go in the backward direction a point x,y can obtained from either
        x-y, y or x, y-x
        Note that the question gurantees that both tx,ty and sx,sy > 0 i,e at a time only x-y or y-x can be +ve.
        Hece in the backwards direction we can discard either one of the pair depending on x>y or y>x
        This makes the backward algorithm Linear.

        Observation-2
        In the backwards direction, say x>y so we can trace back the earlier point to x-y,y. Say x-y is still > y then we
        can do x-2y, y.... and so on, in gneral we can keep subtracting y as long as the x coordinate is greater than y.
        so x,y <---- x-ky, y s.t x-ky < y, in other word we can reduce x,y to x%y, y
        
        Observeration-3
        As we reduce x,y <- x%y, y or x, y%x depending on x>y or y>x there is a chance that we reduce x or y to less than sx
        or sy. So we need to have extra checks. If we can do that in the following way:
        if say x==sx i,e we have matched the x coordinate, the only we can now reduce y to sy is by constantly subtracting x
        in other words (y-sy) should be a multiple of x i,e (y-sy)%x == 0.
        '''
        while tx >= sx and ty >= sy:
            if tx == sx:
                return (ty-sy) % tx == 0
            elif ty == sy:
                return (tx-sx) % ty == 0
            elif tx > ty:
                tx, ty = tx%ty, ty
            elif ty > tx:
                tx, ty = tx, ty%tx
            else:
                break
        return tx == sx and ty == sy