"""
 Paint House II
Solved
Hard
Topics
conpanies icon
Companies
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
Return the minimum cost to paint all houses.

 

Example 1:

Input: costs = [[1,5,3],[2,9,4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
Example 2:

Input: costs = [[1,3],[2,4]]
Output: 5
 

Constraints:

costs.length == n
costs[i].length == k
1 <= n <= 100
2 <= k <= 20
1 <= costs[i][j] <= 20
"""
class Solution:
    """
    This is a simple extension of paint_house.py 
    Time: O(N*K^2)
    """
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        for house in range(1, n):
            for color in range(k):
                # Compute costs[house][color] the cost of painting house # with color
                # Find the min(costs[house-1][color_last != color])
                min_cost = float('inf')
                for last_color in range(k):
                    if last_color == color:
                        continue
                    else:
                        min_cost = min(min_cost, costs[house-1][last_color])
                costs[house][color] += min_cost
        # do the same for last house
        return min(costs[-1])
