# 	Minimum time required to rot all oranges

from queue import Queue


class Solution:
    def isValid(self, x, y, n, m):
        return x >= 0 and y >= 0 and x < n and y < m

    def checkAll(self, grid, n, m):
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return False
        return True

    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])

        q = Queue()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.put([i, j])

        time = 0  # to calculate the time
        while len(q.queue) != 0:
          #  print(q.queue)
            rotted = False  # to check if we have rotted any orange or not
            for i in range(len(q.queue)):
                x, y = q.get()

                # moving in 4 directions
                for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if self.isValid(x + i, y + j, n, m):
                        if grid[x + i][y + j] == 1:
                            # if we are rotting the orange for the first time
                            # then we have used a unit time and within this unit time
                            # other neighboring fresh oranges are also rotted
                            if not rotted:
                                time += 1
                                rotted = True
                            grid[x + i][y + j] = 2
                            q.put([x + i, y + j])

        return time if self.checkAll(grid, n, m) else -1
