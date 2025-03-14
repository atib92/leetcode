"""
Source: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/ 
Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
 

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
"""
class TrieNode():
    def __init__(self, name):
        self.name = name
        self.directory = False
        self.children = {}
class Solution:
    _all_directories = []
    def print(self, s):
        # print(s)
        pass
    def _create_path(self, root, path):
        if root.directory == True:
            self.print(f'{root.name} is already a directory. Early exit !')
            return # Already a parent directory exists.
        node = root.children.get(path[0])
        if node is None:
            node = TrieNode('/' + path[0])
            self.print(f'create {root.name} -> {node.name}')
            root.children[path[0]] = node
        if len(path) == 1:
            self.print(f'Set as directory {node.name}')
            node.directory = True
            return
        else:
            return self._create_path(node, path[1:])
    
    def insert_directory(self, root: TrieNode, directory: str):
        path = directory.strip('/').split('/') # "/a/b" -> [a,b]
        # traverse the path
        self.print(f'Insert path {path}')
        return self._create_path(root,path)

    def get_all_directories(self, root, path=''):
        self.print(f'root: {root.name} path: {path} dir: {root.directory}')
        if root.directory == True:
            self._all_directories.append(path)
            return
        else:
            for child in root.children:
                self.get_all_directories(root.children[child], path=path+root.children[child].name)

    def removeSubfolders(self, directories: List[str]) -> List[str]:
        """
        Algo: The cental concept of the algorithm is a Trie. Every directory is a Trie Node. e.g /a/b/c is Trie Root -> TridNode(a) -> TridNode(b) -> TrieNode(c)
        and the last node of a valid directory is marked as a "directory". Think of it has marking end of words (eow) in a standard trie of words.

        There is one nuance change though. The datastructure for a node's children is a dictionary/hash as opposed to array[26] for a typical charecter based trie.
        This is done since each directory name can be a string in itself and we would also want to go from any directory to any sub-directory in O(1)

        Now the algo works as follows:
        Trie Creation : For every path in the input, we try to create the path in the Trie. This is basically inserting TriedNodes as we traverse an input path. The tweak is as follows:
        During traversal if we enouncter a node which is already marked a directory, we are sure that this is going to be the parent directory of the directory we are in
        the insertion process of so we do not go any further.

        Finding all parent directories: Since we have only populated parent directores in the Trie, this comes down to just a traversal of all possible paths in the trie. We do that
        recursively by keeping a track of "prefixes" and populate the complete path in an instance variable which we return at the end.

        TODO(future): Find a way of solving the problem w/o "not inserting sub-directories".

        """
        # Create the Trie structure that will be used for this problem.
        self._all_directories = []
        root = TrieNode('root')
        for directory in directories:
            self.print(f'Insert directory {directory}')
            self.insert_directory(root, directory)
        self.get_all_directories(root)
        self.print(self._all_directories)
        return self._all_directories
