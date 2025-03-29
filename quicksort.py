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
        i, pivot = low - 1, high
        for j in range(low, high):
            if arr[j] <= arr[pivot]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
        return i+1
