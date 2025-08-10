"""
Zigzag Conversion
Solved
Medium
Topics
conpanies icon
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


"""
O(1) Space ! No Grid required ! Simple O(N) Time, Deterministic Algorithm without creating the Grid

atib
50 Days Badge 2025
0
a few seconds ago
Python3
Intuition
The string index that populates the (imaginary) grid is deterministic and hence do not necessarily require populating the grid

Approach
N: Number of Rows
L: Lenght of the string
Define DELTA = 2(N-1)
The rows will look like this:
row 0 elements :
k*DELTA for k in [0,1,2,...]

row N-1 elements:
i + k*DELTA for k in [0,1,2...]

row i (all middle rows):
i - k * DELTA, i + k * DELTA for k in [0,1,2...]

0 <-Delta-> 8
1         7 9
2       6   10     14
3     5     11  13
4 <-Delta-> 12
Complexity
Time complexity:
O(N) Go over the input string once

Space complexity:
O(1) Constant space (over the space required for the ouput, No extra grid)

Code
"""
class Solution:
    def convert(self, s: str, N: int) -> str:
        if N <= 1:
            return s
        L = len(s)
        output = []
        delta = 2*(N-1)
        # row 0
        k = 0
        while(k*delta < L):
            output.append(s[k*delta])
            k += 1
        # row 1 to n-2
        for i in range(1, N-1):
            k = 0
            while(k*delta - i < L):
                if 0 <= k*delta - i < L:
                    output.append(s[k*delta - i])
                if 0 <= k*delta + i < L:
                    output.append(s[k*delta + i])
                k += 1
        # row n-1
        k = 0
        while(N-1+k*delta < L):
            output.append(s[N-1+k*delta])
            k += 1
        return ''.join(output)
