"""
Word Search II
Solved
Hard
Topics
conpanies icon
Companies
Hint
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
"""
from typing import List, Set
from collections import deque

class TrieNode():
    def __init__(self, value=None) -> None:
        self.value = value
        self.eow = None
        self.children = [None] * 26

class Trie():
    def __init__(self) -> None:
        self.root = TrieNode()
    def insert(self, word) -> None:
        node = self.root
        for ch in word:
            id = ord(ch) - ord('a')
            if node.children[id] is None:
                node.children[id] = TrieNode(value=ch)
            node = node.children[id]
        node.eow = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Doing BFS from each cell for each word is too expensive. Rather we store all
        words in a trie and for each cell, launch a search. A search continues for only
        a cell that is a valid child in the trie node.
        """
        def dfs(r, c, node):
            ch = board[r][c]
            if node.children[ord(ch)-ord('a')] is None:
                return
            else:
                if node.children[ord(ch)-ord('a')].eow is not None:
                    found_words.add(node.children[ord(ch)-ord('a')].eow)
                #else:
                save = board[r][c]
                board[r][c] = "#"
                for rr, cc in [(-1,0), (+1,0), (0,-1), (0,+1)]:
                    r_bar, c_bar = r + rr, c + cc
                    if 0 <= r_bar < R and 0 <= c_bar < C and board[r_bar][c_bar] != "#":
                        dfs(r_bar, c_bar, node.children[ord(ch)-ord('a')])
                board[r][c] = save
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        R, C = len(board), len(board[0])
        found_words = set([])
        for r in range(R):
            for c in range(C):
                dfs(r, c, self.trie.root)
        return list(found_words)
