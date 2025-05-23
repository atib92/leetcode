""" Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

class Solution:
    """ 
    Algo: If input list is of length N, there are total 2 ^ N sets in the power set. In binary format they range from 000..0 to 111..1.
    In other words if we can get the entire binary range from 000...000 to 111...111 then all we need to do is for any binary string
    10101..01 the corresponding subset can be obtatained by including elements from the input array where the corresponding binary string
    has a 1 and exluding the elements from the input array where the corresponding binary string has a 0. Example: if nums = [a,b,c], N = 3
    so there are 2^3=8 subsets from 000, 001, 010, .. 111. A 010 means ['b'], a 110 means ['a', 'b'] and so on.
    """
    def _to_subset(self, num, nums):
        index = len(nums) - 1
        subset = []
        while(num != 0):
            div = num % 2
            num = num // 2
            if div != 0:
                subset.append(nums[index])
            index -= 1
        return subset
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [] 
        N = len(nums)
        for n in range(2 ** N):
            power_set.append(self._to_subset(n, nums))
        return power_set


"""
Notes:
If you think about the above solution, what we essentially did was flattened out all the possible recursions and iterated over them.
For example: if you think f("abc") to be the union of f("bc") once with "a" and once without "a" i,e {"a" X f("bc)} U {f"bc"} (X: Cross Product, U: Union)
you can come up with a simpler true recursive solution
"""
class PowerSet():
    def _powerset(self, s, index):
        print(f'PowerSet for {s[index:]}')
        if len(s[index:]) == 0:
            return [""]
        else:
            res = self._powerset(s, index+1)
            out = [s[index] + _s for _s in res]
            return res + out

    def powerset(self, s):
        return self._powerset(s, 0)

"""
The recursive solution also allows to extend the algo. to when there are duplicates in the string"
Just sort the starting string, so that all duplicates are next to each other and in the recursive
call, skip all duplicate recursion.
"""
class PowerSetWithDuplicates():
    def _powerset(self, s, index):
        print(f'PowerSetDuplicates for {s[index:]}')
        if len(s[index:]) == 0:
            return [""]
        else:
            inc = 1
            # Go ahead until the next charecter is not a duplicate.
            while(index + inc < len(s) and  s[index+inc] == s[index]):
                inc += 1
            res = self._powerset(s, index+inc)
            out = [s[index] + _s for _s in res]
            return res + out

    def powerset(self, s):
        s = sorted(s)
        return self._powerset(s, 0)
