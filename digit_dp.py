"""
Count Numbers with Non-Decreasing Digits 
Hard
You are given two integers, l and r, represented as strings, and an integer b. Return the count of integers in the inclusive range [l, r] whose digits are in non-decreasing order when represented in base b.
An integer is considered to have non-decreasing digits if, when read from left to right (from the most significant digit to the least significant digit), each digit is greater than or equal to the previous one.
Since the answer may be too large, return it modulo 109 + 7.

Example 1:
Input: l = "23", r = "28", b = 8
Output: 3

Explanation:

The numbers from 23 to 28 in base 8 are: 27, 30, 31, 32, 33, and 34.
Out of these, 27, 33, and 34 have non-decreasing digits. Hence, the output is 3.
Example 2:

Input: l = "2", r = "7", b = 2
Output: 2
Explanation:

The numbers from 2 to 7 in base 2 are: 10, 11, 100, 101, 110, and 111.
Out of these, 11 and 111 have non-decreasing digits. Hence, the output is 2.
 

Constraints:

1 <= l.length <= r.length <= 100
2 <= b <= 10
l and r consist only of digits.
The value represented by l is less than or equal to the value represented by r.
l and r do not contain leading zeros.
"""
class Solution:
    def _to_base_10_num(self, l: str):
        num, power = 0, 0
        for ch in l[-1::-1]:
            num += int(ch) * pow(10, power)
            power += 1
        return num

    def _to_base_b_string(self, l_base_10_int: int, b: int):
        print(f'base 10 {l_base_10_int}')
        l_base_b_string = ""
        while(l_base_10_int != 0):
            remainder = l_base_10_int % b
            l_base_10_int = l_base_10_int // b
            l_base_b_string = str(remainder) + l_base_b_string
        print(f'base {b} is {l_base_b_string}')
        return l_base_b_string

    @cache
    def _countNumbers(self, num: str, d: int, base: int, floor: int, tight: bool):
        """
        This is the heart of the digit dp problem.
        Args:
          num : The actual number string in base b. This is required so that we can easily access individual digits in the original number.
          d: This is the number of digits yet to insert. Ex: For a 4 digit number d goes from 4->3->2->1->0
          floor: This is the minimum digit we can insert at a particular position. This is constrained by the problem since we are interested
                 in numbers with digits in non-decreasing order. So subsequent recursions will place this constraint on the next digit position
                 depending on what number we place at the current position. E.g If we place a '4' now, the next number must be one of [4,5,6,... b-1]
          tight: This is the conventional tight constraint argument in a digit dp. If set this means there is a strict constraint on this position
                 which requires us to be strictly <= the corresponding digit in the input number, else we can go as high as possible (ofcurse within
                 what the base 'b' allows)

        Recursion:
          floor is the input argument
          ceil is either the base max (i,e base - 1) or the corresponding digit in the input number if there is a tight constraint
          We are free to pick any digit floor to ceil but once we do that we have to pass the floor in the recursion accordingly.
          floor in the recursion becomes the digit we have chosen in the current position (since next digit cannot be lower than this)
          tight: If we were not in a tight constraint, we will not be in tight constrain in the subsequent call.
                 If we were in tight constraint, we will only be in tight constraint in the subsequent call if we have pick the exact same digit for this position as in the input number,
                 ex: If input nubmer was --56- and we have picked --4-- , we can choose any number after 4 in the subsequent recursion but if we picked --5-- we cannot go above 6.
        """
        if d == 0:
            return 1
        else:
            # num = 5463
            ans = 0
            ceil = int(num[len(num) - d]) + 1 if tight else base
            for digit in range(floor, ceil):
                ans += self._countNumbers(num, d-1, base, digit, tight and (digit == int(num[len(num) - d])))
            return ans

    def countNumbers(self, l: str, r: str, b: int) -> int:
        """
        Algorithm: Digit DP
        Step 1 : Convert the stringified base 10 numbers to stringified base 'b' numbers
        Step 2 : Apply the Digit DP algo on the base b numbers. 


        Future Improvements:
        1. Is it possible to convert from base 10 to base b w/o converting the base10 string to an integer ?
        2. Is it possible to subtract 1 from the base 10 string w/o converting to an integer
        """
        l_base_10_int = self._to_base_10_num(l)
        l_base_b_str = self._to_base_b_string(l_base_10_int-1, b) # We do L-1 since we are interesed in the closed interval [L,R] i,e including L
        
        r_base_10_int = self._to_base_10_num(r)
        r_base_b_str = self._to_base_b_string(r_base_10_int, b)

        nl, nr = len(l_base_b_str), len(r_base_b_str)

        f_ll = self._countNumbers(l_base_b_str, nl, b, 0, True)
        f_rr = self._countNumbers(r_base_b_str, nr, b, 0, True)
        return (f_rr - f_ll) % (10**9 + 7) # if we didn't do L-1 above, this would exclude L from the computation.
