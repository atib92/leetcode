"""
Source: https://leetcode.com/problems/minimum-cost-to-make-array-equal/

You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.
Example 1:

Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.
Example 2:

Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.
 

Constraints:

n == nums.length == cost.length
1 <= n <= 105
1 <= nums[i], cost[i] <= 106
Test cases are generated in a way that the output doesn't exceed 253-1
"""
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        @cache
        def f(x):
            # O(N) : Total cost to make all elems in nums = x
            return sum([abs(nums[i]-x)*cost[i] for i in range(n)])
        n = len(nums)
        low = min(nums) - 1
        high = max(nums) + 1
        while(low < high):
            mid = (low + high) >> 1
            if f(mid) < f(mid+1):
                # on the right side
                high = mid
            else:
                low = mid + 1
        return f(high)
"""
Explantion: if you plot cost curve (i,e a graph when on X axis are the target value that you convert all elements in the nums array to and Y axis is the correspoinding cost),
you get a U shaped curve. This is because the cost curve is a Convex function with a global minima. The global minima is basically the value to which if we convert all the
values of the nums array, we incur the minimum cost.

The U shaped curve has the following property:
LEFT SIDE : f(x) > f(x+1)
RIGHT SIDE: f(x) < f(x+1)

So we denote the property f(x) > f(x+1) as + and f(x) < f(x+1) as -, we can denote the curve as : LEFT + + + + + + + - - - - - - - RIGHT
and the objective is to find the first '-' i,e where f() changes sign !!

Now if we selec the MID = (LOW+HIGH) // 2 s.t
f(mid) > f(mid+1): We know 'mid' is in the RIGHT side so we can continue searching the optima in (MID+1, HIGH) i,e we know the sign has not toggled at mid so we are safe to search from MID+1 to HIGH 
f(mid) < f(mid+1): We know 'mid' is in the LEFT side so we can continue searching the optima in the right side, (LOW, MID) i,e we know the sign has toggled at mid (but we are not sure if it has toggled at mid or before mid) so search LOW, MID

We continue this until LOW < HIGH, the loop ends with HIGH pointing to the global optima.

"""
