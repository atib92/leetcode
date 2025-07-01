"""
 Next Permutation
Solved
Medium
Topics
premium lock icon
Companies
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Insight:
        Let's look at all the permuations of [1,2,3]
        1 : 1 2 3
        2 : 1 3 2
        3 : 2 1 3
        4 : 2 3 1
        5 : 3 1 2
        6 : 3 2 1
        We can see the next lexicographically higher permuation is obtained by moving a larger number to the left of a smaller number s.t there is no permutation lexicographically higher obtainable by moving
        some other larger number to the left, in other words we need to move a larger number to the left and a smaller number to the right such that its lexicographically just more by 1.
        If no such move is possible, example 321 i,e when the array is sorted in descending order, the next is the first / base permutation.

        Using the above insight we develop the following algo:
        1. Start from the right and find the first occurance (i, i+1) s.t arr[i] < arr[i+1]. Since we are starting from the right, if we find such a pair we know we can obtain a lex. higher permutation
           if we swap arr[i] with an element from i+1:N which is > than arr[i] but minimum in the list of all elements in arr[i+1:] that is > arr[i] (Finding the minium element to the right of i which
           is still greater than arr[i]). Call this index j
        2. if we swap arr[i] and arr[j] i,e move arr[i] which is smaller to the right of arr[j] we get a lexicographically higher permuation.
        3. Once we have done the swap we know that the arr[i+1:N] is in descending order (since i,i+1 was the first pair where are[i] < arr[i+1). So just need to revers arr[i+1:] to get the minimum
           permutation of arr[i+1:N]. Techinically you need to sort arr[i+1:] but its already in descending order so just reversing would suffice.
        """
        N = len(nums)
        break_point = None
        for i in range(N-2,-1,-1):
            if nums[i] < nums[i+1]:
                break_point = i
                break
        #print(f'break_point {break_point}')
        if break_point is None:
            nums.sort()
            #print(nums)
        else:
            # Find the minimum value in arr[i+1:] s.t that is > arr[i]
            index = i+1
            for j in range(i+1, N):
                if nums[j] > nums[break_point]:
                    index = j
            nums[i], nums[index] = nums[index], nums[i]
            # i+1 to N is already sorted in reverse order, we just need to reverse it
            low, high = i+1, N-1
            while(low < high):
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1
