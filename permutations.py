""" Given a string s, which may contain duplicate characters, your task is to generate and return an
    array of all unique permutations of the string. You can return your answer in any order.
"""
class Solution:
    def findPermutation(self, word):
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
