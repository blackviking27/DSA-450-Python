# Find the no. of Islands

class Solution:
    def dfs(self, row, col):
        self.visited[row][col] = True
        
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]
        
        for k in range(8):
            x = row + rowNbr[k]
            y = col + colNbr[k]

            if x >= 0 and x < self.rows and y >= 0 and y < self.columns:
                if not self.visited[x][y] and self.grid[x][y] == '1':
                    self.dfs(x, y)

    def numIslands(self, grid):
        self.grid = grid
        self.rows, self.columns = len(grid), len(grid[0])
        self.visited = [[False]*self.columns]*self.rows
        count = 0
        for row in range(self.rows):
            for col in range(self.columns):
                if not self.visited[row][col] and self.grid[row][col] == '1':
                    self.dfs(row, col)
                    count += 1
        return count