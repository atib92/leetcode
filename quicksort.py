class Solution:
    def quickSort(self,arr,low,high):
        """
        Uses lomuto partion algo https://www.geeksforgeeks.org/lomuto-partition-algorithm/
        """
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot-1)
            self.quickSort(arr, pivot+1, high)
    def partition(self,arr,low,high):
        # Pivot Selection: Select the last element as the pivot. We will find the right position for the pivot
        # Everthing to the left of 'i' (<=i) is smaller than the pivot so by the time we are done we can be sure we can insert pivot at 'i+1'
        i, pivot = low - 1, high
        for j in range(low, high):
            # This should be moved to the left of what would be the final position of pivot
            if arr[j] <= arr[pivot]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # We know everthing < pivot is available left of 'i' (including 'i'). Lets move the pivot to its right position
        arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
        return i+1
