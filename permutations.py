""" Given a string s, which may contain duplicate characters, your task is to generate and return an
    array of all unique permutations of the string. You can return your answer in any order.
"""
class Solution:
    def findPermutation(self, word):
        """
        The idea is to generate the permutations of xyz a.k.a f(xyz) by pivoting each char as the first
        char and appending with the permutations of the remaining string i,e [x+f(yz) + y+f(xz) + z + f(xy)]
        We can play with Sets <-> Lists depending on how we want to treat repeats. 
        """
        __all__ = []
        if len(word) <= 1:
            __all__.append(word)
        else:
            for index, char in enumerate(word):
                subwords = self.findPermutation(word[:index]+word[index+1:])
                for subword in subwords:
                    __all__.append(char+subword)
        return list(set(__all__))

""" Given an array nums of distinct integers, return all the possible 
    permutations You can return the answer in any order.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        __all__ = []
        if len(nums) <= 1:
            __all__.append(nums)
        else:
            for index, pivot in enumerate(nums):
                sub_nums = self.permute(nums[:index] + nums[index+1:])
                for sub_num in sub_nums:
                    __all__.append([pivot] + sub_num)
        return __all__

"""
When the input contains duplicate chars
"""
class Solution:
    def _permute(self, s):
        _all_ = []
        if len(s) == 1:
            _all_.append(s)
        else:
            pivot = None
            for index, char in enumerate(s):
                # This is similar to the power set problem when the input has duplicates.
                # We don't need to compute all permutations when a char has been already
                # used as a pivot earlier. Sorting the input string allows us to hop over
                # all duplicate pivots.
                if char == pivot:
                    continue
                else:
                    pivot = char
                    ret = self._permute(s[:index] + s[index+1:])
                    for r in ret:
                        _all_.append(pivot + r)
        return _all_
    def findPermutation(self, s):
        return self._permute(''.join(sorted(s)))
