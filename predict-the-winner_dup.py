"""
 Predict the Winner
Solved
Medium
Topics
conpanies icon
Companies
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

 

Example 1:

Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.
Example 2:

Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
"""
class Solution:
    """
    The idea is pretty simple, if you observe making the greedy choice (choosing max from either end of the array) is not a winning strategy.
    So we need to check all possible outcomes. Doing that by recursion is exponential so we do through top down DP. The DP constrction looks like this:
    dp[i][j] is the max player can accumulate between [i,j] closed interval
    We know dp[i+1][j] and dp[i][j-1] that we can make the right decision. This alredy sounds like the largest palindrome problem where you need to build
    smaller segment first and use the results to build larger segment.
    1. Find optimal strategy for nums[i:j] and use that build the optimal strategy for larger segments dp[i+1:j] and dp[i:j+1]
    """
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            # Optimal strategy for a segment of length 1 is to pick it.
            dp[i][i] = nums[i]
            # Optimal strategy for a segment of length 2 is to pick the max.
            if i + 1 < n:
                dp[i][i+1] = max(nums[i], nums[i+1])
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                # Optimal strategy for i,j :
                # Pick i, but then the 2nd player can either pick i+1 or j 
                # Pick j, but then the 2nd player can either pick i or j-1
                # For each, min(X,Y) denote the maximum score P2 can accumulate and HENCE WE PICK THE MINIMUM !
                dp[i][j] = max(nums[i]+min(dp[i+2][j],dp[i+1][j-1]), nums[j]+min(dp[i][j-2], dp[i+1][j-1]))
        return dp[0][n-1] >= sum(nums) / 2 
