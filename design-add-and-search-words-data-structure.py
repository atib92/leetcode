'''
 Design Add and Search Words Data Structure
Solved
Medium
Topics
conpanies icon
Companies
Hint
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
'''

class TrieNode:
    def __init__(self):
        #self.val = val
        self.eow = False
        self.children = [None] * 26
class WordDictionary:

    def __init__(self):
        '''
        Add words to a Trie dB.
        '''
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Add word to the trie
        node = self.root
        for ch in word:
            index = ord(ch)-ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.eow = True
        

    def search(self, word: str) -> bool:
        def _search(node, word, i, n):
            if i >= n:
                return node.eow == True
            if word[i] == '.':
                for j in range(26):
                    if node.children[j] is not None:
                        if _search(node.children[j], word, i+1, n) == True:
                            return True
            else:
                index = ord(word[i])-ord('a')
                if node.children[index] is not None:
                    if _search(node.children[index], word, i+1, n) == True:
                        return True
            return False
        node = self.root
        return _search(node, word, 0, len(word))


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)