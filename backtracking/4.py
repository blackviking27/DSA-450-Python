# Solve the Sudoku

class Solution:

    def isValid(self, val, row, col, grid):
        # function to check if we can place "val" at (row, col in grid
        for i in range(9):
            # checking rows
            if grid[row][i] == val:
                return False

            # checking columns
            if grid[i][col] == val:
                return False

            # checking the 3x3 box
            if grid[3 * (row // 3) + i // 3][3*(col // 3) + i % 3] == val:
                return False

        return True

    def SolveSudoku(self, grid):
        # looping through each element to find the empty space
        for i in range(9):
            for j in range(9):

                # if empty space
                if grid[i][j] == 0:

                    # trying every number in the from 1 to 9
                    for val in range(1, 10):
                        if self.isValid(val, i, j, grid):
                            grid[i][j] = val
                            # if valid solution is obatined using the current value
                            if self.SolveSudoku(grid):
                                return True
                            else:
                                # if no valid solution is obtained
                                grid[i][j] = 0
                    # if no value can be placed
                    return False
        # if all the values are filled
        return True
