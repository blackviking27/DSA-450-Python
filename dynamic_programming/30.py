# Minimum removals from array to make max –min <= K

def find_j(arr, i, n, k):
    idx = -1 # the value of j

    start = i + 1
    end = n - 1

    while start < end:
        mid = start + (end - start)//2
        if arr[mid] - arr[i] <= k:
            idx = mid # updating the idx value
            start = mid + 1
        else:
            end = mid
    return idx 

def min_removal(arr, k):
    ans = float('inf')
    arr.sort()
    n = len(arr)
    for i in range(n):
        # finding the max j index such that arr[i] -arr[j] <= k
        j = find_j(arr, i, n, k)
        if j != -1:
            ans = min(ans, n-(j - i + 1))
    return ans

# Driver code
a = [1, 3, 4, 9, 10, 11, 12, 17, 20]
k = 4

print(min_removal(a, k))