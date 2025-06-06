"""
 Valid Parentheses
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
class Solution:
    def match(self, left: str, right: str):
        if left is '(' and right is ')':
            return True
        elif left is '{' and right is '}':
            return True
        elif left is '[' and right is ']':
            return True
        else:
            return False

    def is_left(self, ch: str):
        return ch == '(' or ch == '[' or ch == '{'

    def is_right(self, ch: str):
        return ch == ')' or ch == ']' or ch == '}'

    def isValid(self, s: str) -> bool:
        """
        Algo: Enque left parenthesis to a stack, Deque matching parenthesis. Return False if there is a mis-match
        """
        stack = []
        for ch in s:
            if self.is_left(ch):
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                else:
                    pop = stack.pop()
                    if not self.is_left(pop):
                        return False
                    elif not self.match(pop, ch):
                        return False
        return len(stack) == 0
