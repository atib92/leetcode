"""
"""
lass Solution:
    def twoSumNaive(self, nums: List[int], target: int) -> List[int]:
        """
        Naive two loop method Time : O(N*2) Space: O(N)
        """
        N = len(nums)
        for i in range(N):
            for j in range(N):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        The idea is to iterate over the input array and cache the index of elements seen thus far.
        At any time while checking arr[i], if target-arr[i] is detected in the cache, we have found
        the two indices.
        Time: Linear O(N) for traversal * O(1) for lookup in the map = O(N)
        Space: Extra space for cache/map/dict O(N)
        """
        seen = dict()
        for index, elem in enumerate(nums):
            if target-elem in seen:
                return [seen[target-elem], index]
            else:
                seen[elem] = index
