"""
Source : https://leetcode.com/problems/domino-and-tromino-tiling/description/
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 10^9 + 7.
In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.
"""
class Solution:
    def _to_int(self, direction:bool) -> int:
        if direction == True:
            return 1
        else:
            return 0

    def get_key(self, n:int, up:bool, down:bool):
        _up, _down = self._to_int(up), self._to_int(down)
        return f'{n}-{_up}-{_down}'

    def numTilings(self, n: int) -> int:
        self.cache = {}
        return self._numTilings(n)

    def _numTilings(self, n, up=False, down=False):
        """
        Algo: There are basically these patterns that we can apply using the doming or the trimino
        1. | : Just one vertical domino
        2. -- : Just one horizontal domino
        3. = : Two horizontal domino stacked vertically
        4. L : A trimino that leaves a gap at the top
        5. A trimino that leaves a gap at the bottom 

        Given these we can create sub-problems like follows : 
        At any point if there is no gap from the prev step we can add 1. or 3. or 4. or 5. Note Adding 4. and 5. adds a gap that needs to be propagated ahead.
        At any point if there is a gap, we should fill the gap. Ex: If ther is a gap at the top, we can add 2. and propagate a bottom gap further OR add a trimino that fills the gap and propagete further.
        """
        if n < 0:
            return 0
        elif n == 0 and up is False and down is False:
            return 1
        else:
            key = self.get_key(n, up, down)
            ret = self.cache.get(key)
            if ret is None:
                if up is False and down is False:
                    ret = self._numTilings(n-1) + self._numTilings(n-2) + self._numTilings(n-2, up=True) +  self._numTilings(n-2, down=True)
                elif up is False and down is True:
                    ret = self._numTilings(n-1, up=True) + self._numTilings(n-1)
                elif up is True and down is False:
                    ret = self._numTilings(n-1, down=True) + self._numTilings(n-1)
                else:
                    ret = 0
                self.cache[key] = ret
            return ret % 1_000_000_007 # Do not store the module ans in the cache since module is not additive.
    
