# K-th Largest Sum Contiguous Subarray

import heapq


def kth_largest_sum(arr, n, k):
    prefix_sum = [arr[0]]  # taking zero and first element

    for i in range(1, n):
        prefix_sum.append(prefix_sum[i - 1] + arr[i])

    # heap
    q = []
    heapq.heapify(q)

    for i in range(n):
        for j in range(i, n):
            temp = prefix_sum[j] - (prefix_sum[i - 1] if i != 0 else 0)

            if len(q) < k:
                heapq.heappush(q, temp)
            else:
                if q[0] < temp:
                    heapq.heappop(q)
                    heapq.heappush(q, temp)

    return q[0]


arr = [10, -10, 20, -40]
n = 4
k = 6
print(kth_largest_sum(arr, n, k))
