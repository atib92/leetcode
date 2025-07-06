"""
Find the K-th Character in String Game II
Solved
Hard
Topics
conpanies icon
Companies
Hint
Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k. You are also given an integer array operations, where operations[i] represents the type of the ith operation.

Now Bob will ask Alice to perform all operations in sequence:

If operations[i] == 0, append a copy of word to itself.
If operations[i] == 1, generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word. For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
Return the value of the kth character in word after performing all the operations.

Note that the character 'z' can be changed to 'a' in the second type of operation.

 

Example 1:

Input: k = 5, operations = [0,0,0]

Output: "a"

Explanation:

Initially, word == "a". Alice performs the three operations as follows:

Appends "a" to "a", word becomes "aa".
Appends "aa" to "aa", word becomes "aaaa".
Appends "aaaa" to "aaaa", word becomes "aaaaaaaa".
Example 2:

Input: k = 10, operations = [0,1,0,1]

Output: "b"

Explanation:

Initially, word == "a". Alice performs the four operations as follows:

Appends "a" to "a", word becomes "aa".
Appends "bb" to "aa", word becomes "aabb".
Appends "aabb" to "aabb", word becomes "aabbaabb".
Appends "bbccbbcc" to "aabbaabb", word becomes "aabbaabbbbccbbcc".
 

Constraints:

1 <= k <= 1014
1 <= operations.length <= 100
operations[i] is either 0 or 1.
The input is generated such that word has at least k characters after all operations.
"""


"""
Intuition
The brute force is ofcourse to run through the transformations one by one but note that the lenght of the string doubles after every transformation so this will end up being O(2^N) and time out at scale.

The key to solving this recursively w/o having to compute all intermediate strings is to notice that the kth char after the mth transformation is derived from the k'th char after the m-1the transformation. The solution then boils down to formulazing this relationship

Approach
No of transformations M from #0, #1 ... #M-1
Length of string after mth transformation is pow(2, m+1)
Note that char 'i' after m-1th transformation maps to 'i'th and 'i + pow(2, m)' th char after the mth operation. The latter is either the same char or the char+1 depending on if the mth operation is 1/0
The base case is when m < 0 which we know is the single char string "a"
Complexity
Time complexity:
O(N): We recurse over the the input transformation array

Space complexity:
O(N): Stack space for the recursion.
Could easily be O(1) if we do this iteratively.
"""
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def charshift(shift):
            return chr(ord('a') + (shift % 26))
        def kth_char_after_mth_operation(k, m, shift):
            if m < 0:
                return charshift(shift)
            else:
                mid = pow(2, m)
                if k >= mid:
                    k -= mid
                    if operations[m] == 1:
                        shift += 1
            return kth_char_after_mth_operation(k, m-1, shift)
        M = len(operations) # Total number of operations
        return kth_char_after_mth_operation(k-1,M-1,0)
