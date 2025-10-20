"""
Letter Combinations of a Phone Number
Solved
Medium
Topics
conpanies icon
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

# Strategy: Simple BFS
from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        __mapping__ = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        q = deque()
        i, n = -1, len(digits)
        q.append((-1,'')) # Bootstrap by enqueing an empty string
        out = []
        while(q):
            index, combination = q.popleft()
            if index == n-1:
                out.append(combination)
            else:
                for ch in __mapping__[digits[index+1]]:
                    q.append((index+1, combination+ch))
        return out

# Time: O(4^N)
# Space: O(4^N) Since every combination is stored 
