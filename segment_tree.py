"""
Segment Tree program to find out SUM in [low, high]
"""
def create_segment_tree(arr, low, high, st, index):
    if low == high:
        # Leaf node
        st[index] = arr[low]
    elif low < high:
        mid = (low + high) // 2
        l = create_segment_tree(arr, low, mid, st, 2*index+1)
        r = create_segment_tree(arr, mid+1, high, st, 2*index+2)
        st[index] = l + r
    return st[index]

def find_sum_in_range(low, high, index, arr, range_low, range_high):
    if range_low <= low and range_high >= high:
        return st[index]
    elif range_low > high or range_high < low:
        return 0
    else:
        # Range is completely within the low-high
        mid = (high + low) // 2
        l = find_sum_in_range(low, mid, 2*index+1, arr, range_low, range_high)
        r = find_sum_in_range(mid+1, high, 2*index+2, arr, range_low, range_high)
        return l+r

if __name__ == "__main__":
    arr = [4,3,12,1,0,-5,3,5,6]
    #      0 1 2  3 4 5  6 7 8
    N = len(arr)
    st = [0]*(4*N)
    create_segment_tree(arr, 0, N-1, st, 0)
    test_cases = [
            [0,1,7],
            [2,5,8],
            [5,8,9]
    ]
    for index, tc in enumerate(test_cases):
        s = find_sum_in_range(0, N-1, 0, arr, tc[0], tc[1])
        if s != tc[2]:
            print(f'Test #{index} FAILED. Range {tc[0]}-{tc[1]} Expected {tc[2]} Got {s}')
        else:
            print(f'Test #{index} PASSED Range {tc[0]}-{tc[1]} Result : {s}!')
"""
OUTPUT:
(env) mdatib-HM95H402GV:CODING mdatib$ python sum_segment_tree.py 
Test #0 PASSED Range 0-1 Result : 7!
Test #1 PASSED Range 2-5 Result : 8!
Test #2 PASSED Range 5-8 Result : 9!
"""



#2 Program to find MINIMUM in [low, high]
def build_segment_tree(st, arr, index, low, high):
    if low == high:
        # Leaf node
        value = arr[low]
    elif low > high:
        return float("inf")
    else:
        mid = (low + high) // 2
        left = build_segment_tree(st, arr, 2*index+1, low, mid)
        right = build_segment_tree(st, arr, 2*index+2, mid+1, high)
        value = min(left, right)
    st[index] = value
    return value

def constructST(arr, n):
    st = ["inf"] * (4*n)
    build_segment_tree(st, arr, 0, 0, n-1)
    return st

def SRQ(st, arr, index, low, high, range_start, range_end):
    if range_start <= low and range_end >= high:
        return st[index]
    elif low > range_end or high < range_start:
        return float("inf")
    else:
        mid = (low + high) // 2
        left = SRQ(st, arr, 2*index+1, low, mid, range_start, range_end)
        right = SRQ(st, arr, 2*index+2, mid+1, high, range_start, range_end)
        return min(left, right)

if __name__ == "__main__":
    arr = [1,2,3,4]
    st = constructST(arr, 4)
    n = 4
    print(SRQ(st, arr, 0, 0, n-1, 2, 3))
