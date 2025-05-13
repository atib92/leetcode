"""
Maximum Points You Can Obtain from Cards
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
 

Constraints:

1 <= cardPoints.length <= 105
1 <= cardPoints[i] <= 104
1 <= k <= cardPoints.length
"""

class Solution:
    """
    The Naive approach is to start with l = 0 and r=N-1 and recurse:
    find_max_score(l,r,k) = max(find_max_score(l+1, r, k-1), find_max_score(l, r-1, k-1))
    This works for smaller sized arrays but times out at high scale since Time = O(2^K) = O(2^N) exponential.

    Optimal approach: There is a structure to this problem which can help reduce the time complexity from exponential to linear. If you 
    think about this the exponential basically allows you to pick/select any elements in a pure random setting. However in this problem,
    you the subarray you end up with after you remove the prefix and suffic subarrays is contigous which makes the exponential algo an
    over kill.

    You can imaging that if you remove k_bar elements from the begining of the array, you can only remove the last k-k_bar elemets from
    the end of the array i,e the mid section of the array will always have n-k number of contigous elements. So that's what we will do.
    We will start with an empty prefix array so that the first n-k elemnts are the mid array and the remaining elements are the end array.
    At each step we will compute the sum of the mid section and using that we will derive the sum of the suffix and prefix array which
    is nothing but total_sum - mid_section_sum. We do that until there is no suffix array and return maximum sum of the prefix+suffix
    array seen in the entire exercise.

    Note: The problem is very similar to max sum subarray of lenght k except that this time we want to maximimze the complement of the
    mid section array.

    Note: The algo become linear we can compute the sum upfront and then update the mid section sum by removing the old element from
    the head and adding the new element from the tail.
    """
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        <---k_bar (A) ---><----- n-k ------><--- k - k_bar (B) ---->
        The idea is to find such a k_bar so that A+B is maximized
        Lets start the n-k subarray from first index i,e A=NULL MID= [0,n-k] B= remaining k elements
        and goes all the way such that A=firs k chars and mid starts from k+1
        k_bar = 0
        A = arr[:0] Empty
        mid = arr[0:n-k]

        k_bar = 1
        A = arr[:1] first element
        mid = arr[1:n-k+1]

        k_bar = 2
        A = arr[:2] first 2 elments
        mid = arr[2:n-k+2]
        """
        n = len(cardPoints)
        mid = sum(cardPoints[:n-k])
        total = mid + sum(cardPoints[n-k:])
        s = total - mid
        for k_bar in range(1, k+1):
            mid = mid - cardPoints[k_bar-1] + cardPoints[n-k+k_bar-1]
            s = max(s, total - mid)
        return s
