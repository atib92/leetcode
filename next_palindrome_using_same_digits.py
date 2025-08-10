"""
Next Palindrome Using Same Digits
Solved
Hard
Topics
conpanies icon
Companies
Hint
You are given a numeric string num, representing a very large palindrome.

Return the smallest palindrome larger than num that can be created by rearranging its digits. If no such palindrome exists, return an empty string "".

A palindrome is a number that reads the same backward as forward.

 

Example 1:

Input: num = "1221"
Output: "2112"
Explanation: The next palindrome larger than "1221" is "2112".
Example 2:

Input: num = "32123"
Output: ""
Explanation: No palindromes larger than "32123" can be made by rearranging the digits.
Example 3:

Input: num = "45544554"
Output: "54455445"
Explanation: The next palindrome larger than "45544554" is "54455445".
 

Constraints:

1 <= num.length <= 105
num is a palindrome.
"""



"""
Intuition
This is similar to next lexicographically higher sequence except with the added constraint of palindromic pattern.

Approach
To get the lexicographically next sequence, we need to move a larger number from a lesser significant position to higher significant position and vice versa for a smaller number. The idea is to be able to pick up this pair so that we really only get the immediate next higher and don't skip some sequences.

For example: This of this pattern 543212345, take the first half (before the pivot) 5432, this is already sorted in descending order, you cannot re-order 5432 to get a slightly higher number but think of 45544554 and its first half 4554, you can immedate think of 5544, 5445 as alternate first halves that form a palindrome each higher than the input so how do we arrive at the lexico next i,e 5445 ?
You need to combine these two points:

Move left in the first half, if you see a pair of numbers ...LARGER,SMALLER... as seen above this can be re-arranged to get a higher no
If you see a pair of number ...SMALLER,HIGHER... you have an opportunity to swap them to achive a higher palindromic seqence. But as we saw this might not be the very next higher sequence. To get the immmediate next, you need to swap SMALLER with the minimum number from HIGHER.... which is greater than SMALLER. E.g : 35421 you see [35] is the SMALLER:HIGHER pair, in this case '3' is swapped with '4' to get 45321 (Note how 5321 is sorted in descending order, to get the minimum just reverse it to 1235) so the swapped sequence becomes 35421->41235
Complexity
Time complexity:
O(N)
Space complexity:
O(N)
Code
"""

class Solution:
    def nextHalfPalindrome(self, num:List[str]):
        n = len(num)
        i = n-2
        while(i >= 0 and num[i] >= num[i+1]):
            i -= 1
        if i < 0:
            return False
        else:
            j = n-1
            while(num[j] <= num[i]):
                j -= 1
            num[i], num[j] = num[j], num[i]
            num[i+1:] = num[i+1:][::-1]
            return True
    def nextPalindrome(self, num: str) -> str:
        half = list(num[:len(num)//2])
        ret = self.nextHalfPalindrome(half)
        if ret == True:
            if len(num) % 2 == 0: # even length
                return ''.join(half) + ''.join(half[::-1])
            else: # odd length
                return ''.join(half) + num[len(num)//2] + "".join(half[::-1])
        else:
            return ""


"""
