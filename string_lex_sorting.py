"""
A simple lex sort of strings. The idea is to store the strings in a Trie and just traverse it which organically sorts the strings in lexicographic order.
Future implementation: Handle duplicates, Handle captial letters, etc...
"""
class TrieNode():
    def __init__(self, value):
        self.value = value
        self.eow = False
        self.children = [None] * 26

class Trie():
    def __init__(self):
        self.root = TrieNode(None)

    @staticmethod
    def _get_index(char):
        return ord(char) - ord('a')

    def insert_word(self, s):
        node = self.root
        for ch in s:
            index = self._get_index(ch)
            if node.children[index] is None:
                node.children[index] = TrieNode(ch)
            node = node.children[index]
        node.eow = True

    def search_word(self, s):
        node = self.root
        for ch in s:
            index = self._get_index(ch)
            if node.children[index] is None:
                return False
            node = root.children[index]
        return node.eow == True

    def _traverse(self, node, prefix):
        if node is None:
            return
        else:
            for child in node.children:
                if child is not None:
                    if child.eow is True:
                        print(f'{prefix+child.value}\n')
                    self._traverse(child, prefix+child.value)

    def traverse(self):
        return self._traverse(self.root, '')


class Solution():
    def sort(self, strings):
        print(f'Input String {strings}')
        trie = Trie()
        for s in strings:
            trie.insert_word(s)
        return trie.traverse()


if __name__ == "__main__":
    sol = Solution()
    sorted_strings = sol.sort(["axd", "abl", "cxt", "cxa"])
    print(sorted_strings)

"""
Input String ['axd', 'abl', 'cxt', 'cxa']
abl

axd

cxa

cxt
"""
