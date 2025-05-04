"""
Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.
"""

class Solution:
    def _twoSum(self, target, arr, avoid):
        _map = {}
        for index, val in enumerate(arr):
            if index == avoid:
                continue
            else:
                if target-val in _map:
                    return True
                else:
                    _map[val] = index
        return False
    def hasTripletSum(self, arr, target):
        """
        We iterate over the input array and for each element, we basically solve the 2sum problem for target-arr[i]
        The one point to note is that when solving the 2sum problem, we cannot consider the ith index. We take care
        of that using the "avoid" index in the _twoSum.
        """
        for index, val in enumerate(arr):
            if self._twoSum(target-val, arr, index):
                return True
        return False

"""
Another way to solve it to iterate over the array like the above but rather than solving 2sum using hashing, 
we can sort the input array and solve the 2sum using 2 pointer approach. In total there would be 3 pointers,
i : Pivot pionter.
Given i, find Target - arr[i] in arr[j:k]

a. sort the input array
b. iterate using i
c. for every i, start with j=i+1 and k = N-1 i,e the first and last elments of the array after i.
d. At any step if sum of elems at i, j, k == 0, we have found one combination.
e. At any step if sum of elems at i, j, k < Target, we need to increase the sum, hence move j forward (note: arr is now sorted to going right of j is going to increse the sum)
f. At any step if sum of elems at i, j, k > target, we need to decrease the sum, hence move k backwards ( note: arr is now sorted to going left of k is going to decrese the sum)

Note: While moving i and j make sure they are different from their earlier valus to detect only distinct combination.
"""
class Solution:
    """
    Target = 0
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums = sorted(nums)
        i = 0
        results = []
        for i in range(N):
            #print(f'i {i} nums {nums}')
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = N-1
            while(j < k):
                s = nums[i] + nums[j] + nums[k]
                if s == 0: # Target is Zero but could be anything.
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while(j < k and nums[j] == nums[j-1]):
                        j += 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return results
