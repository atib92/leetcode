"""
Number of Provinces
Solved
Medium
Topics
Companies
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""
class Solution:
    def _merge_provinces(self, p_a, p_b):
        # We find the smaller and larger indicies so that we cleanly update the lower index'ed province/set
        # and remove the list element corresponding to the larger indexed set cleanly. To improve, we can
        # keep a hash map of which city belongs to which province so that _find_province_index become O(1)
        if p_a < p_b:
            p_s, p_l = p_a, p_b
        elif p_a > p_b:
            p_s, p_l = p_b, p_a
        else:
            return
        self.provinces[p_s] =  self.provinces[p_s].union(self.provinces[p_l])
        self.provinces.pop(p_l)
    def _find_province_index(self, city):
        for province_index, province in enumerate(self.provinces):
            if city in province:
                return province_index
    def merge_cities(self, city_a, city_b):
        p_a = self._find_province_index(city_a)
        p_b = self._find_province_index(city_b)
        return self._merge_provinces(p_a, p_b)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        The no. of provinces are basically the number of connected components in the graph.
        We can solve this using "Union Find". The algo will work as follows:
        1. Start with provinces = [set(0), set(1), .. set(N)] i,e N provinces/sets
        2. Go through the adj matrix and for each edge a-b, Find the corresponding provinces, p_a, p_b.
        3. If p_a, p_b are same, continue. Else: Add the cites from p_b to p_a and delete p_b form the list of provinces.
        4. After we are done, the provinces list will only contain diconncted provinces
        """
        n = len(isConnected)
        self.provinces = [{i} for i in range(n)]
        for src_city in range(n):
            for dst_city in range(src_city+1, n):
                if isConnected[src_city][dst_city] == 1:
                    self.merge_cities(src_city, dst_city)
        return len(self.provinces)
