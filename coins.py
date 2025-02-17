""" Given some coin denominations e.g [1,2,5] find how many ways can you create N dollars."""

class Solution:
    """ 
    This at first might sound identical to the "ladder problem" (see ladder.py) i,e f(N) = f(N-1) + f(N-2) + f(N-5)
    but there is a subtle but important difference from the ladder problem. Think of going up by 5 steps in the
    ladder when you are allowed steps [1,2,5].. Seq [1,2,2] and [2,2,1] are two diffrent ways to reach step 5 but
    in the context of bulding $5 using deonimations of [1,2,5], the two combinations [1,2,2] and [2,2,1] are identical !
    Hence if we simply re-use the ladder code here we will end counting a combination multiple times.
    So, how do we avoid duplicates ?
    Well, one way to do it is to first compute how to many $1 to $N with only the least denomiation and then introduce the
    next higher denomination and so on.... that would allow the combination [1,2,2] but not [2,2,1] or [2,1,2] a.k.a we
    need to swap the order of the nested dp loop.
    """
    def change(self, amount, coins):
        dp = [1] + [0 for i in range(amount)]
        for coin in coins:
            for amt in range(1, amount+1):
                if amt-coin >= 0:
                    dp[amt] += dp[amt-coin]
        return dp[amount] 
