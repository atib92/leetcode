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


# FOLLOWUP
"""
Say you are also given a list of valid words and only those combinations are valid.

1. One way to approach that would be find all combinations and filter (post-processing) only the valid ones. [VERY WASTEFUL]
2. A better elimination strategy would be to discard any wip combination that will never match a valid combination.
At any point in time we have : (index, wip_combination) 
if wip_combination is not a valid prefix of any valid combination, we can safely discard it
2a. Whenever enqueing a new wip_combination, check if its a valid prefix 
BETTER - TRIE PRUNING
2b. Keep a TRIE of valid words and pass along the trie node as part of the wip_combination
e.g say a valid combination is abcd and our wip_combination is ab:
If the current digit has a 'c' and only If the current trie node has a child 'c', will we enque 'abc'
"""
from collections import deque
from typing import List

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [None]*26
        self.eow = False
class Trie:
    def __init__(self):
        self.root = TrieNode('-1')
    def insert_word(self, word):
        node = self.root
        for ch in word:
            if node.children[ord(ch)-ord('a')] is None:
                node.children[ord(ch)-ord('a')] = TrieNode(ch)
            node = node.children[ord(ch)-ord('a')]
        node.eow = True

class Dialpad:
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
        q.append((-1,''))
        out = []
        while(q):
            index, combination = q.popleft()
            if index == n-1:
                out.append(combination)
            else:
                for ch in __mapping__[digits[index+1]]:
                    q.append((index+1, combination+ch))
        return out

    def letterCombinations_v2(self, digits: str, valid_words) -> List[str]:
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
        i, n = -1, len(digits)
        q = deque()
        trie = Trie() 
        for word in valid_words:
            trie.insert_word(word)
        q.append((-1, trie.root, ''))
        out = []
        while(q):
            index, node, wip_combination = q.popleft()
            if index == n-1:
                if node.eow == True:
                    out.append(wip_combination)
            else:
                for ch in __mapping__[digits[index+1]]:
                    if node.children[ord(ch)-ord('a')] is not None:
                        q.append((index+1, node.children[ord(ch)-ord('a')], wip_combination+ch))
        return out

dp = Dialpad()
words = dp.letterCombinations('23')
print(words)

words = dp.letterCombinations_v2('23', ['ae', 'ad', 'cd'])
print(words)

(env) mdatib-HM95H402GV:CursorPlayGround mdatib$ python phone_number.py 
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
['ad', 'ae', 'cd']
