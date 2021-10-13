# Partition array to K subsets

class Solution:

    # s_idx -> pointing to the current set
    def solve(self, s_idx):
        # base condition
        # if the sum of current subset is the required sum
        if self.subSet[s_idx] == self.sum:
            # if we have found k - 1 equal subsets
            # note: comparig with k - 2 since we have 0-based indexing
            if s_idx == self.k - 2:
                return True

            return self.solve(s_idx + 1)

        # going through each element
        for i in range(self.n):
            if not self.vis[i]:
                if self.subSet[s_idx] + self.arr[i] <= self.sum:

                    self.vis[i] = True
                    self.subSet[s_idx] += self.arr[i]

                    temp = self.solve(s_idx)

                    self.vis[i] = False
                    self.subSet[s_idx] -= self.arr[i]
                    if temp:
                        return True
        return False

    def isKPartitionPossible(self, a, k):
        # we have to make just 1 subset
        if k == 1:
            return True

        self.n = len(a)

        # if number of subsets required is greater than number of elements
        # then we cannot form an answer
        if k > self.n:
            return False

        s = 0
        for el in a:
            s += el

        # if we cannot equally divide into subsets
        if s % k != 0:
            return False

        self.sum = s // k  # sum of each set
        self.arr = a  # array
        self.k = k  # number of subsets

        # to know if we have included the element into the answer
        self.vis = [False] * self.n
        self.subSet = [0] * k

        # initialising the result with first element
        self.vis[0] = True
        self.subSet[0] = self.arr[0]

        return self.solve(0)
