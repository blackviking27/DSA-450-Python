# Partition Equal Subset Sum

class Solution:
    def equalPartition(self, N, arr):
        self.arr = arr

        # taking total sum
        s = 0
        for el in arr:
            s += el

        # if sum is odd then we cannot divide the array
        if s % 2 != 0:
            return False
        # dp to store the precomputed result
        self.dp = [[-1 for _ in range(s//2 + 1)] for _ in range(N)]
        return self.solve(N - 1, s//2)

    def solve(self, idx, s):
        # if we have traversed through all the elements in the array
        if idx == -1:
            # if we able to find the sum 's'
            if s == 0:
                return True
            # if not able to find
            return False

        if s == 0:
            return True  # if we find the sum 's'
        if s < 0:
            return False  # if we are not able find the sum

        if self.dp[idx][s] != -1:
            return self.dp[idx][s]

        # checking if we are to find the solution when we include 'idx' element
        # or when we dont include 'idx' element
        self.dp[idx][s] = self.solve(
            idx - 1, s - self.arr[idx]) or self.solve(idx - 1, s)
        return self.dp[idx][s]
