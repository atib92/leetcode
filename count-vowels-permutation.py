'''
Count Vowels Permutation
Solved
Hard
Topics
Hint
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4
'''

class Solution:
    '''
    Rules:
        Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
        Each vowel 'a' may only be followed by an 'e'.
        Each vowel 'e' may only be followed by an 'a' or an 'i'.
        Each vowel 'i' may not be followed by another 'i'.
        Each vowel 'o' may only be followed by an 'i' or a 'u'.
        Each vowel 'u' may only be followed by an 'a'.
    '''
    def countVowelPermutation_recursive(self, n: int) -> int:
        '''
        Simple recursive approach (with caching)
        f(ch, k) repesents ways to form a string with k chars s.t the last
        charecter is ch.
        '''
        MOD = pow(10,9)+7
        @cache
        def f(ch, k):
            if k == 0:
                return 1
            else:
                if ch == 'a':
                    return f('e', k-1) % MOD
                elif ch == 'e':
                    return f('a', k-1) % MOD + f('i', k-1) % MOD
                elif ch == 'i':
                    return f('a', k-1)% MOD + f('e', k-1)% MOD + f('o', k-1)% MOD + f('u', k-1)% MOD
                elif ch == 'o':
                    return f('i', k-1)% MOD + f('u', k-1)% MOD
                elif ch == 'u':
                    return f('a', k-1)% MOD
        count = 0
        for ch in "aeiou":
            count += f(ch, n-1) % MOD 
        return count % MOD

    def countVowelPermutation(self, n: int) -> int:
        '''
        a - > e
        e - > a, i
        i - > a, e, o, u
        o - > i, u
        u - > a

        The rules can be stated the other way like this:

        e,i,u -> a
        a,i   -> e
        e,o   -> i
        i     -> o
        i,o   -> u

        In other words, we can only place an 'a' if the preceding letter is one of e,i,u
        and so on and so forth.

        This time we try to place letters iteratively (n times) and we use the count from the
        prev round

        '''
        MOD = 10**9 + 7
        # Number of permuations of length 1 ending with these letters is just 1
        a = e = i = o = u = 1

        for _ in range(n - 1):
            na = (e + i + u) % MOD
            ne = (a + i) % MOD
            ni = (e + o) % MOD
            no = i % MOD
            nu = (i + o) % MOD

            a, e, i, o, u = na, ne, ni, no, nu

        return (a + e + i + o + u) % MOD