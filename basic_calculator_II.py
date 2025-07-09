"""
 Basic Calculator II
Solved
Medium
Topics
conpanies icon
Companies
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    def print(self, s:str):
        #print(s)
        pass
    def calculate(self, s: str) -> int:
        def compute(a, b, ch):
            if ch == '/':
                return a // b
            elif ch == "*":
                return a * b
            elif ch == "+":
                return a + b
            elif ch == "-":
                return a - b
            else:
                print('Unsupported operator {ch}. Returning None to fail explcitly')
                return None 
        def precedence(ch):
            # The problem does a bad job explaining that div, mul have the same priority
            # and needs to be computed left to right (and not like standard BODMAS). Same
            # for add,sub
            if ch == '/':
                return 0
            elif ch == "*":
                return 0
            elif ch == "-":
                return -1
            elif ch == "+":
                return -1
            else:
                self.print('Unsupported operator {ch}. Returning None to fail explcitly')
                return None            
        processed_list = []
        num_string = ''
        # pre process the input first to club together multi digit numbers
        # "3 +21* 2" -> [3, +, 21, * , 2]
        for ch in s:
            if ch == ' ':
                continue
            elif ch == '*' or ch == '/' or ch == '+' or ch == '-':
                processed_list.append(num_string)
                processed_list.append(ch)
                num_string = ''
            else:
                num_string += ch
        processed_list.append(num_string)
        self.print(processed_list)
        operator_stack, operator_tos = [], -1
        operand_stack, operand_tos = [], -1
        i, N = 0, len(processed_list)
        while(i < N):
            ch = processed_list[i]
            if ch == '*' or ch == '/' or ch == '+' or ch == '-':
                # if precedence is same, we need to compute left to right so treat it same as if
                # the tos has a higher precedence operator.
                while(operator_tos > -1 and precedence(ch) <= precedence(operator_stack[-1])):
                    operator = operator_stack.pop()
                    operator_tos -= 1
                    b = operand_stack.pop()
                    a = operand_stack.pop()
                    operand_tos -= 2
                    operand_stack.append(compute(a, b, operator))
                    operand_tos += 1
                operator_stack.append(ch)
                operator_tos += 1
            else:
                # operand
                operand_stack.append(int(ch))
                operand_tos += 1
            i += 1
        self.print(f'operand_stack {operand_stack} tos {operand_tos}')
        self.print(f'operator_stack {operator_stack} tos {operator_tos}')
        while(operator_tos > -1):
            operator = operator_stack.pop()
            operator_tos -= 1
            b = operand_stack.pop()
            a = operand_stack.pop()
            operand_tos -= 2
            operand_stack.append(compute(a, b, operator))
            operand_tos += 1
        return operand_stack[-1]
