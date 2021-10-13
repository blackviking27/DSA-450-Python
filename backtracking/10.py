# Find shortest safe route in a path with landmines

from collections import deque  # for BFS approach

# DFS approach


class DFS:

    def isSafe(self, x, y):
        if x >= 0 and x < self.n and y >= 0 and y < self.m:
            return True
        return False

    def markUnsafe(self, grid):
        # function which marks the unsafe place in grid
        for i in range(self.n):
            for j in range(self.m):

                if grid[i][j] == 0:

                    for dx, dy in self.dir:
                        if self.isSafe(i + dx, j + dy):
                            grid[i + dx][j + dy] = -1

        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == -1:
                    grid[i][j] = 0

    def solve(self, row, col, dist, grid):
        # base case, we have reached the last column in the grid
        if col == self.m - 1:
            self.min = min(self.min, dist)
            return

        # if the dist is greater than he current dist
        # then we need not check in this path
        if dist > self.min:
            return

        # marked visited since it is included in the path now
        self.vis[row][col] = True

        for dx, dy in self.dir:
            x = row + dx
            y = col + dy
            if self.isSafe(x, y):
                if grid[x][y] != 0 and not self.vis[x][y]:
                    self.solve(x, y, dist + 1, grid)

        # backtracking
        self.vis[row][col] = False

    def shortestPat(self, grid):
        self.n = len(grid)  # rows
        self.m = len(grid[0])  # cols

        # min dist
        self.min = float('inf')

        # to know if  we have visited the position or not
        self.vis = [[False for _ in range(self.m)] for _ in range(self.n)]

        # four directions we can move to
        self.dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        self.markUnsafe(grid)

        # going through each row in first column
        for i in range(self.n):
            if grid[i][0] == 1:
                self.solve(i, 0, 0, grid)

        print(self.min)


# BFS approach
class BFS:

    def markUnsafe(self, grid):
        # function which marks the unsafe place in grid
        for i in range(self.n):
            for j in range(self.m):

                if grid[i][j] == 0:

                    for dx, dy in self.dir:
                        if self.isSafe(i + dx, j + dy):
                            grid[i + dx][j + dy] = -1

        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == -1:
                    grid[i][j] = 0

    def shortestPath(self, grid):
        self.markUnsafe(grid)

        n = len(grid)
        m = len(grid[0])

        dist = [[-1 for _ in range(m)] for _ in range(n)]

        q = deque()

        # for every 1 in the first column
        for i in range(self.n):
            # saving i, j
            q.append([i, 0])
            dist[i][0] = 0

        while q:
            i, j = q.popleft()
            d = dist[i][j]
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x = i + dx
                y = j + dy
                if x >= 0 and x < n and y >= 0 and y < m:
                    if grid[x][y] == 1 and dist[x][y] == -1:
                        dist[x][y] = d + 1
                        q.append([x, y])

        ans = float('inf')
        for i in range(n):
            if grid[i][m - 1] == 1 and dist[i][m - 1] != -1:
                ans = min(ans, dist[i][m - 1])

        print(ans)
