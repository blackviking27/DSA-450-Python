# Merge two binary Max heaps

class Solution():

    # percolate up for the current index
    def heapify(self, arr, idx, n):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != idx:
            arr[largest], arr[idx] = arr[idx], arr[largest]
            self.heapify(arr, largest, n)

    def mergeHeaps(self, a, b, n, m):

        # adding both the array to create a new array
        a = a + b
        n = len(a)

        # heapifying every non leaf node in the new array
        for i in range(n//2 - 1, -1, -1):
            self.heapify(a, i, n)
        # print(a)
        return a
