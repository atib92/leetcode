"""
 Word Ladder
Solved
Hard
Topics
Companies
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
rom collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Simple BFS: Change each char one by one to generate new words and if the new word
        is a valid word (in the library) put in the queue to repeat and find all its neighbors.
        """
        library = set(wordList) # A set for faster membership check
        q = deque()
        seen = set()
        q.append((beginWord, 1))
        seen.add(beginWord)
        while(q):
            word, num = q.popleft()
            if word == endWord:
                return num
            else:
                for i, ch in enumerate(word):
                    # There can be 5000 valid words but the len of each word at max can be 10 so doing the char by char
                    # check is much better than checking all possible valid words again every current word
                    for j in range(ord('a'), ord('z')+1):
                        # You can keep a check here for chr(j) != ch but not required since we later check new_word in seen before enqueing.
                        new_word = word[:i] + chr(j) + word[i+1:]
                        if new_word in library and not new_word in seen:
                            seen.add(new_word)
                            q.append((new_word, num+1))
        return 0
