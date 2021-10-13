# Print all possible paths from top left to bottom right of a mXn matrix

class Solution:

    # i, j is the position in matrix and pi points to the current position in path array
    # which can be filled. The path is stored in path[0...pi - 1]
    def solve(self, i, j, pi):
        # if we have reached the last row
        if i == self.m - 1:
            for k in range(j, self.n):
                self.path[pi + k - j] = self.matrix[i][k]

            # printing the solution
            for l in range(pi + self.n - j):
                print(self.path[l], end=" ")
            print()
            return

        # if we have reached the last column
        if j == self.n - 1:
            for k in range(i, self.m):
                self.path[pi + k - i] = self.matrix[k][j]

            # printing the solution
            for l in range(pi + self.m - i):
                print(self.path[l], end=" ")
            print()
            return

        # adding the current element to the path
        self.path[pi] = self.matrix[i][j]

        # moving down
        self.solve(i + 1, j, pi + 1)

        # moving right
        self.solve(i, j + 1, pi + 1)

        # if diagonal is also allowed
        # self.solve(i + 1, j + 1, pi + 1)

    def printAllPath(self, matrix, m, n):
        self.m = m
        self.n = n

        self.matrix = matrix

        self.path = [0 for _ in range(n + m)]  # to store the paths

        self.solve(0, 0, 0)


s = Solution()
arr = [[1, 2, 3],
       [4, 5, 6]]

s.printAllPath(arr, 2, 3)
