'''
Count and Say
Solved
Medium
Topics
conpanies icon
Companies
Hint
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

 

Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:

Input: n = 1

Output: "1"

Explanation:

This is the base case.

 

Constraints:

1 <= n <= 30
 

Follow up: Could you solve it iteratively?
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        # count and say array
        c = [None] * (n+1)
        c[1] = "1"
        def rle(input_string: str) -> str:
            '''
            Input: Input string
            Output: RLE encode string
            '''
            s = input_string + '0' # Senitel
            count = 1
            last = s[0]
            output = [] # mutable structure. Convert finally to string buffer.
            for ch in s[1:]:
                if ch == last:
                    count += 1
                else:
                    output.extend([str(count), last])
                    count = 1
                    last = ch
            return ''.join(output)
        for num in range(2, n+1):
            c[num] = rle(c[num-1])
        return c[-1]


