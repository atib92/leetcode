"""
 Largest Component Size by Common Factor
Solved
Hard
Topics
conpanies icon
Companies
You are given an integer array of unique positive integers nums. Consider the following graph:

There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:


Input: nums = [4,6,15,35]
Output: 4
Example 2:


Input: nums = [20,50,9,63]
Output: 2
Example 3:


Input: nums = [2,3,6,7,4,12,21,39]
Output: 8
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 105
All the values of nums are unique.
"""
import math

class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [p for p in range(self.n)]
        self.size = [1] * self.n
        self.largest_component = 1
    def find(self, x):
        p = self.parent[x]
        if p != x:
            self.parent[x] = self.find(p)
        return self.parent[x]
    def union(self, x, y):
        xrep, yrep = self.find(x), self.find(y)
        if xrep != yrep:
            if self.size[xrep] >= self.size[yrep]:
                self.size[xrep] += self.size[yrep]
                self.largest_component = max(self.largest_component, self.size[xrep])
                self.parent[yrep] = xrep
            else:
                self.size[yrep] += self.size[xrep]
                self.largest_component = max(self.largest_component, self.size[yrep])
                self.parent[xrep] = yrep
            return True
        else:
            return False

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        """
        step 1: Create the graph. The output shoud be the adj matrix/list
        step 2: Perform a DSU on the graph and return the largest connected component

        EDIT:
        Step 1 is going to OOM for large graphs. Its much better to find the prime factors of each node
        and maintain a reverse index of prime_factor -> set of indices/nodes which has that factor. 
        Do a DSU Union when we see a factor has common nodes/indices.
        """
        n = len(nums)
        def get_factors(x):
            factors = set()
            d = 2
            while d * d <= x:
                if x % d == 0:
                    factors.add(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                factors.add(x)
            return factors
        factors_to_index = {} # Dict mapping
        dsu = DSU(n)
        for index, num in enumerate(nums):
            factors = get_factors(num)
            for factor in factors:
                # Find all indices that has this factor
                if factor in factors_to_index:
                    for index_dst in factors_to_index[factor]:
                        dsu.union(index, index_dst)
                else:
                    # First time seeing this factor
                    factors_to_index[factor] = [index]
        return dsu.largest_component

