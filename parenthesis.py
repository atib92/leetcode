""" Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""
class Solution:
    @staticmethod
    def _can_insert_left(l,L,r,R):
        # a '(' can only be inserted if
        # L > 0 i,e '(' is available
        return L > 0
    @staticmethod
    def _can_insert_right(l,L,r,R):
        # a ')' can only be inserted if 
        # R > 0 i,e ')' is available and there are enough '(' already added i,e l > r
        return R > 0 and l > r
    def _generateParenthesis(self, prefix, l, L, r, R) -> int:
        """ 
        prefix: The substring so far
        l: Number of left parenthesis used up already
        L: Number of left parenthesis still available
        r: Similar to l but for right parenthesis
        R: Similar to L but for right parenthesis
        L(R) can be derived from n-l(n-R) as well !

        Algorithm: The idea is to try to add a '(' and ')' at each location
        and recusively find all valid parenthesis strings with the remaining
        parenthesis given its possible to add a '('/')' at the said location.
        """
        # Base Cases:
        if L == 0 and R == 0:
            return prefix
        else:
            ret = 0
            l_check = self._can_insert_left(l, L, r, R)
            r_check = self._can_insert_right(l, L, r, R)
            if l_check is True:
                l_ret = self._generateParenthesis(prefix + '(', l+1, L-1, r, R)
                if l_ret:
                    self.all_combinations.append(l_ret)
            if r_check is True:
                r_ret = self._generateParenthesis(prefix + ')', l, L, r+1, R-1)
                if r_ret:
                    self.all_combinations.append(r_ret)
        # Can neighter add a '(' or ')'
        return None

    def generateParenthesis(self, n: int) -> List[str]:
        self.all_combinations = []
        self._generateParenthesis('',0,n,0,n)
        return list(set(self.all_combinations))
""" 
Output:
For n=3
["((()))","(()())","(())()","()(())","()()()"]
"""
        

# Much simpler / cleaner version
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _generateParenthesis(l, r, prefix):
            if l > r:
                return
            elif l == 0 and r == 0:
                combinations.add(prefix)
            else:
                if l > 0:
                    _generateParenthesis(l-1,r, prefix + '(')
                if r > l:
                    _generateParenthesis(l, r-1, prefix + ')')
        combinations = set()
        _generateParenthesis(n,n,'')
        return list(combinations)
