# Combination Sum
# leetcode => https://leetcode.com/problems/combination-sum-ii/

class Solution:

    def solve(self, idx, path, target):
        if target == 0:  # if we have found the target sum
            self.res.append(path[:])
            return

        # making sure we include the current element only in 1 path
        for i in range(idx, self.n):
            # skipping all the same elements to avoid duplicate
            if i > idx and self.arr[i] == self.arr[i - 1]:
                continue

            # if the current element is greater than the target then we can
            # just skip
            if self.arr[i] > target:
                return

            # including in the path
            path.append(self.arr[i])
            self.solve(i, path, target - self.arr[i])
            path.pop()  # backtracking

    def combinationalSum(self, arr, target):
        arr.sort()  # to get the answer in non decreasing order
        self.arr = arr
        self.n = len(arr)

        self.res = []  # to store the result
        self.solve(0, [], target)
