# Max Heap
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def buildHeap(arr):
    n = len(arr)
    idx = len(arr) // 2 - 1
    for i in range(idx, -1, -1):
        heapify(arr, n, i)

    print(arr)


arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
buildHeap(arr)
