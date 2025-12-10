"""
1. Use a result variable to hold the best result seen so far
2. Always use l <= r criteria
3. Always move l, r to l, m-1 or m+1, r to avoid getting caught up in loops.
4. If you need min_greater, max_smaller (i,e without the equality), swap the == scenario in the if-else clause.
"""

def min_greater_equal(arr, target):
    l, r = 0, len(arr)-1
    res = None
    while(l <= r):
        m = (l + r) // 2
        if arr[m] < target:
            l = m+1
        else:
            res = arr[m] # Possible result
            r = m-1
    return res

def max_smaller_equal(arr, target):
    l, r = 0, len(arr)-1
    res = None
    while(l <= r):
        m = (l + r) // 2
        if arr[m] <= target:
            res = arr[m] # Possible result
            l = m+1
        else:
            r = m-1
    return res

if __name__ == "__main__":
    #print(min_greater_equal([10, 20, 30, 40, 50, 60], 44))
    print(max_smaller_equal([10, 20, 30, 40, 50, 60], 70))
