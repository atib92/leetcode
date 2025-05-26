""" Longest Consecutive Sequence
Solved
Medium
Topics
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

--->>>>> You must write an algorithm that runs in O(n) time. <<<<<----

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

class Solution:
    def longestConsecutiveSorting(self, nums: List[int]) -> int:
        """
        O(Nlog) : Sort the input array. Straight forward after that.
        """
        nums = sorted(nums)
        _max = 1
        i = 1
        N = len(nums)
        if N < 1:
            return 0
        prev = nums[0]
        l = 1
        print(nums)
        while(i < N):
            if nums[i] == prev + 1:
                l += 1
            elif nums[i] == prev:
                pass
            else:
                _max = max(_max, l)
                l = 1
            prev = nums[i]
            i += 1
        _max = max(_max, l)
        return _max

    def longestConsecutiveMap(self, nums: List[int]) -> int:
        """
        The idea is to do a one pass and find the min amd max.
        Then you can iterate over all integers beween min and max
        and if a num exists in the hash, the longest streak ending
        at it is the streak ending at 'num-1' + 1

        Its purely O(max) which can potentially be worst than O(N)
        if num[i] >> N which is infact the caser here.

        If the spread in the input data is not much, this technique
        might be efficient.
        """
        numHash = {}
        _min, _max = 1000000000, -1000000000
        for i, num in enumerate(nums):
            numHash[num] = 1
            _max = max(_max, num)
            _min = min(_min, num)
        longest = 0
        for num in range(_min, _max+1):
            if num in numHash:
                if num-1 in numHash:
                    numHash[num] = numHash.get(num-1)+1
                longest = max(longest, numHash[num])
        return longest

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        This is O(N) assuming membership check in sets is O(1) (which it is in Python atleast)
        1. Convert the list to a set for a O(1) lookup
        2. Iterate over the set to find consecutive numbers
        """
        nums = set(nums)
        longest = 0
        for num in nums:
            l = 1
            if num-1 in nums:
                # This is criticial since it avoids re-computing from non streak starting position,
                # Example for [6,7,8], it would only compute for streak starting point '6'.
                continue
            _next = num+1
            while(_next in nums):
                l += 1
                _next += 1
            longest = max(longest, l)
        return longest
