'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
'''

# 1. Recursive SUBOPTIMAL Solution: Time O(2^N)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def _jump(index):
            if index == n-1:
                return True
            elif index >= n or visited[index] == True:
                return False # Taken care of earlier path
            else:
                visited[index] = True
                for j in range(1, nums[index]+1):
                    if _jump(index + j) == True:
                        return True
                return False
        n = len(nums)
        visited = [False]*n
        return _jump(0)


# 2 Optimal : Greedy Solution. Time O(N)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        GREEDY : We just need to track the max index reachable index.
        '''
        furthest_reachable = 0
        n = len(nums)
        for index in range(n):
            if index > furthest_reachable:
                # This means we can not reach this index. If we cannot
                 # reach this index, we can definitely not progress more
                return False
            furthest_reachable = max(furthest_reachable, index+nums[index])
            if furthest_reachable >= n-1:
                return True
        return False