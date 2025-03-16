def _get_left_index(index):
    return (index << 1) + 1

def _get_right_index(index):
    return (index + 1) << 1

def _get_parent_index(index):
    return (index-1) >> 1

def _get_min_child_index(arr, index, L):
    li = _get_left_index(index)
    ri = _get_right_index(index)
    if ri < L:
        if arr[li] < arr[ri]:
            return li
        else:
            return ri
    elif li < L:
        return li
    else:
        return None

def _swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def heapify(arr, index, L):
    next_index = _get_min_child_index(arr, index, L)
    #print("next index {}".format(next_index))
    if next_index is None:
        return
    else:
        if arr[index] > arr[next_index]:
            _swap(arr, index, next_index)
            return heapify(arr, next_index, L)

def build_min_heap(arr):
    index =  _get_parent_index(len(arr)-1) # Parent of last node i,e index len(arr)-1
    L = len(arr)
    while(index >= 0):
        heapify(arr, index, L)
        index -= 1

def heapsort(arr):
    build_min_heap(arr)
    index = len(arr) - 1
    while(index > 0):
        _swap(arr, 0, index)
        heapify(arr, 0, index) # Trap Alert: You can tempted to pass the slice arr[:index] here but swaps won't reflect since python
                               # passed around a new / different referece. So pass the full arr instead !
        index -= 1
    return arr


if __name__ == "__main__":
    arr = [9,4,3,8,10,2,5]
    print(arr)
    print(heapsort(arr))
    print("------------------")
    arr = [1,2,3,3,4,5,6]
    print(arr)
    print(heapsort(arr))
    print("------------------")
    arr = [6,5,4,3,2,1,0]
    print(arr)
    print(heapsort(arr))
