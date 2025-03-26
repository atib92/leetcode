"""
Given n items, each with a specific weight and value, and a knapsack with a capacity of W, the task is to put the items in the knapsack such that the sum of weights of the items <= W and the sum of values associated with them is maximized. 

Note: You can either place an item entirely in the bag or leave it out entirely. Also, each item is available in single quantity.

Examples :

Input: W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1] 
Output: 3
Explanation: Choose the last item, which weighs 1 unit and has a value of 3.
Input: W = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6] 
Output: 0
Explanation: Every item has a weight exceeding the knapsack's capacity (3).
Input: W = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 2, 3] 
Output: 80
Explanation: Choose the third item (value 30, weight 2) and the last item (value 50, weight 3) for a total value of 80.
Constraints:
2 ≤ val.size() = wt.size() ≤ 103
1 ≤ W ≤ 103
1 ≤ val[i] ≤ 103
1 ≤ wt[i] ≤ 103
"""
class Solution:
    def knapsack(self, W, val, wt):
        """
        We have solved the problem in 4 different ways in increasingly more optimal ways.
        """
        #return self.knapsack_simple_recursion(0,0,0,W,val,wt)
        #return self.knapsack_dp_2D(W, val, wt)
        #return self.knapsack_dp_2D_cleaner(W, val, wt)
        return self.knapsack_dp_og(W, val, wt)
        
    def knapsack_simple_recursion(self, w, v, i, W, val, wt):
        """
        This is a very simple (brute-force) recursive solution. At every indel, we make two recursive calls
        corresponding to a. pick b. skip the current index. For N items, this algo is O(2**N) and won't work
        at scale. You could however use memoization to cache already computed values.
        """
        if w > W:
            return 0
        elif i >= len(val):
            return v
        else:
            pick = self.knapsack_simple_recursion(w+wt[i], v+val[i], i+1, W, val, wt)
            skip = self.knapsack_simple_recursion(w, v, i+1, W, val, wt)
            return max(pick, skip)
            
    def knapsack_dp_og(self, W, val, wt):
        """
        This is the OG Dynamic Programming version. You can get rid of "one row for each index" from
        knapsack_dp_2D if you update the same one row. The trick here is that when processing dp[w]
        at index i the skip option is basically the current value of dp[w] (i,e the one computed at
        the earlier iteration i-1) but the pick option requires you knowing dp[w-wi] from the earlier
        iteration but you would have over written it if you coming from left to right. So the trick is
        to populate dp[w] from right to left !
        """
        dp = [0] * (W+1)
        for i in range(len(val)):
            for w in range(W,wt[i]-1,-1):
                dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
        return dp[W]
        
    def knapsack_dp_2D(self, W, val, wt):
        """
        This is a standard bottom-up Dynamic programming approach. You have weights going from 0 to W as columns
        and items going from rows 0 to N-1. At any cells (W,i) we compute the maximum of pick or skip. The extra
        index and weight checks make it a bit ugly so we improve that in the next algo "knapsack_dp_2D_cleaner"
        """
        dp = [[0] * (W+1) for _ in range(len(val))]
        for i in range(len(val)):
            for w in range(W+1):
                skip = 0
                pick = 0
                if i > 0:
                    # We can process skipping and look at prev best
                    skip += dp[i-1][w]
                # We can process keep and look at prev best for adjusted weight
                if w >= wt[i]:
                    pick += val[i]
                    if i > 0:
                        pick += dp[i-1][w-wt[i]]
                dp[i][w] = max(skip, pick)
        return dp[-1][-1]
        
    def knapsack_dp_2D_cleaner(self, W, val, wt):
        """
        This is a cleaner version of "knapsack_dp_2D"
        We keep a dummy first row that saves the hassle of doing the i>0 checks. But does adds complexity that now  you have
        to read val and wt and index i-1
        """
        dp = [[0] * (W+1) for _ in range(len(val)+1)]
        for i in range(1, len(val)+1):
            for w in range(W+1):
                skip = dp[i-1][w]
                if w >= wt[i-1]:
                    pick = val[i-1] + dp[i-1][w-wt[i-1]]
                else:
                    pick = 0
                dp[i][w] = max(skip, pick)
        return dp[-1][-1]
        
