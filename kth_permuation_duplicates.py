"""
Given a string, find the kth lexicographically sorted permuation. The string can have duplicates.
For the case when the string has no duplicates, refer kth_permutation.py. This code is generalization of kth_permutation
for when there are repeat charecters in the input string

I have also added code to generate all permuationns just so that I can test the code.
"""

from collections import Counter
from functools import cache
from typing import List
import unittest

def permutations(s: str) -> List[str]:
    """
    Takes an input string and return a list of all permuations, ex:
    abc -> [abc, acb, bac, bca, cab, cba]
    """
    if not s:
        return []
    else:
        out = []
        prev = None
        for pivot, elem in enumerate(s):
            if elem == prev:
                # Skip the same pivot (for when the input has duplicates)
                continue
            else:
                prev = elem
                sub_permuations = permutations(s[:pivot] + s[pivot+1:])
                if sub_permuations:
                    for sub_permuation in sub_permuations:
                        out.append(elem + sub_permuation)
                else:
                    out.append(elem)
        return out


@cache
def factorial(n: int):
    # At scale, you are better off using math.factorial() inbuilt lib.
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def kth_permuatation_unique(s:str, k:int) -> str:
    """
    This is just the kth_permuation.py repeated here for easy reference !
    
    This function returns the kth permutation in lex. order (zero based indexing)
    Ex: "abc"
    0 abc
    1 acb
    -----
    2 bac
    3 bca
    -----
    4 cab
    5 cba
    For len n string (no duplicates) you can see there are total n! permuations.
    These n! permuations are grouped in n groups of (n-1)! string where mth group
    is nothing but the mth char as pivot and then the (n-1)! permuations of the
    remaining n-1 strings. That gives us a recursive state space.
    kth permuation in the initial n! permuations -> k'th permuation in the (n-1)! permuations -> .... k=1 case!
    n groups: 0,1,2...n-1, group size = (n-1)!
    group - 0 : 0,1,2, (n-1)!-1
    group - 1 : (n-1)!, .... 2*(n-1)!-1
    kth permuation will be in the  group  k // (n-1)! so string[group] will be the pivot
    and the number will be k % (n-1)! element in that group since
    """
    if k == 0:
        return s
    else:
        n = len(s)
        group_size = factorial(n-1)
        pivot = k // group_size
        offset = k % group_size
        return s[pivot] + kth_permuatation(s[:pivot] + s[pivot+1:], offset)


def multinomial(counts: Counter) -> int:
    """Return number of unique permutations for given multiset of chars."""
    n = sum(counts.values())
    denom = 1
    for c in counts.values():
        denom *= factorial(c)
    return factorial(n) // denom

def kth_permuatation(s: str, k: int) -> str:
    """
    The algorithm is a pretty simple extension of kth_permuation_unique once you observe that the groups
    can be unequal sizes depending on the number of times the pivot element exists in the input string.
    We know the formula for total # of permuations when there are repates :
    n!/n1!*n2!... (from math. This is what basically implemented in multinomial function)
    When there are no repates we know from k // (n-1)! which exact group the kth permuation would belong 
    but since groups are of unequal size in this case, we need to traverse group by group (one by one)
    and check if the kth permuation belongs in that groups. As we traverse the groups, we adjust k accordingly
    by the nuber of permuatios we jump over.
    """
    counts = Counter(s)
    total = multinomial(counts)
    if k < 0 or k >= total:
        raise ValueError("k out of range")

    result = []
    while counts:
        for ch in sorted(counts):  # lexicographic order
            if counts[ch] == 0:
                continue
            # try this char as pivot
            counts[ch] -= 1
            block_size = multinomial(counts)
            if k < block_size:
                result.append(ch)
                break
                # This will make the while loop continue over the smaller frequency_counter (since we removed the current ch in line 114)
            else:
                k -= block_size
                # Going to next block so add back the ch we removed from count earlier.
                counts[ch] += 1
        else:
            break
    return "".join(result)


class TestKthPermutation(unittest.TestCase):
    def setUp(self):
        self.s = "aabbcc"
        self.all_permuations = permutations(self.s)
        for index, elem in enumerate(self.all_permuations):
            print(f'{index}: {elem}')
    def test_simple(self):
        k = 10
        print(f'Testing index {89}')
        self.assertEqual(kth_permuatation(self.s, k), self.all_permuations[k])

if __name__ == "__main__":
    unittest.main()
