"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""
class Solution:
    @staticmethod
    def string_to_int(s: str):
            N = len(s)
            num = 0
            for index, char in enumerate(s):
                num += int(char) * pow(10, -index)
            num *= pow(10, N-1)
            return round(num)

    @staticmethod
    def is_char(s:str) -> bool:
        return "a" <= s <= "z"

    @staticmethod
    def is_digit(s:str) -> bool:
        return "0" <= s <= "9"

    def decodeString(self, s: str) -> str:
        """
        Algo :
        1. Keep pushing chars and "[" elements to a stack
        2. When you see a ']'
           i.   Keep popping until tos is a "[", keep concatenating s = popped_string + s
           ii.  Pop out the "["
           iii. Pop out the integer "popped_integer"
           iv.  s = s * popped_integer
           iii. Push s.
           iv. Continue !
        3. finally pop everthing and concatenate to get the output string

        Note: Since the leading integer can be in the range [1,300], we will need an api to
        to convert "123" into 123.
        """
        index = 0
        stack, tos = [], -1 # Note: Using a list and tos variable as a stack. Using a real stack will boost performance.
        while(index < len(s)):
            ch = s[index]
            if self.is_char(ch) or ch == "[":
                stack.append(ch)
                index += 1
                tos += 1
            elif ch == "]":
                temp_s = ""
                while(stack[tos] != "["):
                    temp_s = stack[tos] + temp_s
                    tos -= 1
                    stack.pop()
                # remove "["
                stack.pop()
                tos -= 1
                # remove the integer
                n = stack.pop()
                tos -= 1
                temp_s = temp_s * n
                # Push the string back
                stack.append(temp_s)
                tos += 1
                index += 1
            else:
                # digit
                int_s = ""
                while(self.is_digit(s[index])): # Since the integer can be in the range [1,300] and not a single digit always.
                    int_s += s[index]
                    index += 1
                stack.append(self.string_to_int(int_s))
                tos += 1
        out = ""
        while(tos > -1):
            out = stack.pop() + out
            tos -= 1
        return out
