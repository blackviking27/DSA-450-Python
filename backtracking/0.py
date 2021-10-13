# Rat in a Maze Problem

class Solution:

    def solve(self, i, j, path, m):
        # checking if current position is within the board or not
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return
        
        # if at zero or already visited element
        if m[i][j] == 0 or self.vis[i][j]:
            return

        # if at the (n -1, n-1)
        if i == self.n - 1 and j == self.n - 1:
            self.res.append(path)
            return
        
        # marking the current node as true
        self.vis[i][j] = True
        
        # moving in the four direction in lexiographical order
        self.solve(i + 1, j, path + "D", m)
        self.solve(i, j - 1, path + "L", m)
        self.solve(i, j + 1, path + "R", m)
        self.solve(i - 1, j, path + "U", m)

        # marking the node as false since it will considered in other paths too
        self.vis[i][j] = False


    def findPath(self, m, n):
        self.n = n # length of row and column

        # to know if we have visite current element or not
        self.vis = [[False for _ in range(n)] for _ in range(n)]
        self.res = [] # to store the result

        self.solve(0, 0, "", m)
        return self.res