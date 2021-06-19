# Chocolate Distribution Problem

def findMinDiff(self, arr,N,M):
        if M == 0 or N == 0:
            return 0
        # sort the array
        arr.sort()
        if N < M:
            return -1
            
        # taking the largest minimum difference possible
        min_diff = float('inf')
        # since we take i and i + m - 1,
        # then i +m - 1 should be less than n, thus i + m - 1 = N
        # and this gives us the range i = N -m + 1
        for i in range(N - M + 1):
            min_diff = min(min_diff, arr[i + M - 1] - arr[i])
        return min_diff