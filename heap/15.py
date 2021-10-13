# Convert min Heap to max Heap

class Solution:
    # heapify function
    def heapify(self, idx, arr, n):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != idx:
            arr[idx], arr[largest] = arr[largest], arr[idx]
            self.heapify(largest, arr, n)

    def convert(self, arr, n):
        for i in range(n//2 - 1, -1, -1):
            self.heapify(i, arr, n)
        return arr


# driver code
min_heap = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
n = len(min_heap)

obj = Solution()
print(f"Min Heap : {min_heap}")

print(f"Max Heap : {obj.convert(min_heap, n)}")
