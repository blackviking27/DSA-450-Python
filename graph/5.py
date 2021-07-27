# Rat in a Maze Problem

class Solution:
    def dfs(self,i ,j ,s):
        # if it is feasible to move in any other direction
        if i <0 or j < 0 or i >= self.n or j >= self.n: return

        # if it is already visited or 0
        if self.m[i][j] == 0 or self.vis[i][j] == True: return

        if i == self.n - 1 and j == self.n - 1:
            self.ans.append(s)
            return
        
        self.vis[i][j] = True

        self.dfs(i - 1, j, s + 'U')
        self.dfs(i + 1, j, s + 'D')
        self.dfs(i, j - 1, s + 'L')
        self.dfs(i, j + 1, s + 'R')

        self.vis[i][j] = False


    def findPath(self, m, n):
        self.vis = [[False for _ in range(n)] for _ in range(n)]
        self.m = m
        self.n = n
        self.ans = []

        if self.m[0][0] == 0: return self.ans # if the starting element is zero
        if self.m[n-1][n-1] == 0: return self.ans # if the destination is zero
        s = "" # this stores the path

        self.dfs(0,0, s)
        self.ans.sort()
        return self.ans
