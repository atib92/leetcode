"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        The idea is very simple. At any point if you see a better buy price (lesser than prev buy price), update the buy_price.
        At point if you see a price > buy_price, book profits and update buy_price to the current price as a potentially new
        buy price. (Note: setting/updating buy_price doesn't mean we are buying the stock at that price since we update that
        if we see a lower buy price later.)
        """
        buy_price = float("inf")
        profit = 0
        for price in prices:
            if price < buy_price:
                # Better buy_price
                buy_price = price
            else:
                # book profit
                profit += price - buy_price
                # Potentially buy
                buy_price = price
        return profit 
