"""
In the Tower of Hanoi puzzle, you are given n disks stacked in ascending order (smallest at the top)
on the first of three rods. The goal is to move all disks to the third rod following two rules: only
one disk can be moved at a time, and a disk can only be placed on top of a larger disk. Given the
number of disks n and three rods labeled as from, to, and aux (starting rod, target rod, and auxiliary
rod, respectively),  returns the total number of moves needed to transfer all disks from the starting
rod to the target rod.
"""
class Solution:
    """ 
    Y: Move top N-1 disks from source to aux using destination as the helper
    X: Move the remaining 1 from source to destination
    Z: Move the N-1 disks from aux to destination using source as  the helper
    """
    def towerOfHanoi(self, n, fromm, to, aux):
        if n > 0:
            #      X +     <----------- Y -------------->     +     <--------- Z ------------->
            return 1 + self.towerOfHanoi(n-1, fromm, aux, to) + self.towerOfHanoi(n-1, aux, to, fromm)
        else:
            return 0
