# Tug of War

class Solution:

    def solve(self, idx, s1, s2, set1, set2, arr):
        # base case,
        # we have traversed all the elements in the array
        if idx == self.n:
            if self.min > abs(s1 - s2):
                self.min = abs(s1 - s2)
                self.set1 = set1[:]
                self.set2 = set2[:]

            return

        # if we can fit n//2 elements in the array or not
        if len(set1) < (self.n + 1) // 2:
            # appending the current element to the first set
            set1.append(arr[idx])
            self.solve(idx + 1, s1 + arr[idx], s2, set1, set2, arr)
            set1.pop()  # removing from first set

        if len(set2) < (self.n + 1) // 2:
            # appending the current element to the second set
            set2.append(arr[idx])
            self.solve(idx + 1, s1, s2 + arr[idx], set1, set2, arr)
            set2.pop()  # removing from the second set

    def tugOfWar(self, arr, n):
        self.n = n

        self.min = float('inf')  # stores the min diff between sets

        self.set1 = []
        self.set2 = []

        # parameters in the solve function
        # idx, sum_of_set1, sum_of_set2, set1, set2, arr
        self.solve(0, 0, 0, [], [], arr)

        print(*self.set1)
        print(*self.set2)


s = Solution()
arr = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
n = len(arr)
s.tugOfWar(arr, n)
