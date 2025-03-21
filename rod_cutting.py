"""
Rod Cutting : 
Given a rod of length n(size of price) inches and an array of prices, price. price[i] denotes the value of a piece of length i. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Example:

Input: price[] = [1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
Explanation: The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5+17=22.
Input: price[] = [3, 5, 8, 9, 10, 17, 17, 20]
Output: 24
Explanation: The maximum obtainable value is 24 by cutting the rod into 8 pieces of length 1, i.e, 8*price[1]= 8*3 = 24.
Input: price[] = [1, 10, 3, 1, 3, 1, 5, 9]
Output: 40
Constraints:
1 ≤ price.size() ≤ 103
1 ≤ price[i] ≤ 106
"""

class Solution:
    def cutRod(self, price):
        """
        Approach: Bottom Up Dynamic Programming. max_price[i] stores the optimal solution for rod of length 'i+1', so we just need to return max_price[N-1] once we have computed the array.
        Overlapping sub-problems : The optimal solution for max_price[i] is nothing but the maximum among:
        i. no cut -> price[i]
        ii. cut at length 1 -> max_price[0] + max_price[i-1]
        iii. cut at length 2 -> max_price[1] + max_price[i-2]
        ....
        Basically the problem boils down to how many ways can we sumup to N, eg. for 3 it could 1+1+1, 1+2, 3 which corresponds to 3 cuts of len 1 each, 2 cuts of len 1 and 2 and no cut..
        """
        N = len(price)
        max_price = [price[0]] + [0] * (N - 1)
        for index in range(1,N):
            max_price[index] = price[index]
            j = 0
            while(j <= index - j - 1):
                max_price[index] = max(max_price[index], max_price[j] + max_price[index-j-1])
                j += 1
        return max_price[N-1]
