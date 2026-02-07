'''
4Sum
Solved
Medium
Topics
conpanies icon
Companies
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        4 sum -> 3 sum -> 2 sum (which is solved by 2 pointer method)
        '''
        n = len(nums)
        nums.sort() # O(Nlog(N))
        results = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                # solve 3 pointer problem from i+1 to n-1
                for j in range(i+1, n-2):
                    # solve 2 pointer probem from j+1 to n-1
                    if j > i+1 and nums[j] == nums[j-1]:
                        continue
                    else:
                        l, r = j+1, n-1
                        while l < r:
                            a, b, c, d = nums[i], nums[j], nums[l], nums[r]
                            s = a + b + c + d
                            if s == target:
                                results.append([a,b,c,d])
                                l += 1
                                while l < r and nums[l] == c:
                                    l += 1
                                r -= 1
                                while l < r and nums[r] == d:
                                    r -= 1
                            elif s < target:
                                l += 1
                            else:
                                r -= 1
        return results


