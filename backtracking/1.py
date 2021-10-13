from copy import deepcopy


class Solution:

    # function which generates all the possible solution
    def solve(self, col, board):
        # if we have reached the end then we are able to place all the queens in the correct place
        if col == self.n:
            self.res.append(deepcopy(board))
            return

         # trying to place the queen in any row of 'col' column
        for row in range(self.n):
            # checking if the queen is not attacked by any other queen
            if not self.row[row] and not self.upper_left[col - row + self.n - 1] and not self.down_left[row + col]:

                # marking True so that next queen can check if any queen can attack it or not
                self.row[row] = True
                self.upper_left[col - row + self.n - 1] = True
                self.down_left[row + col] = True

                board[row][col] = "Q"
                self.solve(col + 1, board)
                board[row][col] = "."  # backtracking

                # removed the marks
                self.row[row] = False
                self.upper_left[col - row + self.n - 1] = False
                self.down_left[row + col] = False

    def solveNQueens(self, n):
        self.n = n  # number of rows and columns

        # creating the board
        board = [["." for _ in range(n + 1)] for _ in range(n + 1)]

        self.res = []  # to store the result of the array

        self.row = [False] * n  # to check if  a queen is already at a row
        # to check diagonally up for any queen
        self.upper_left = [False] * (2 * n - 1)
        # to check diagonally down for any queen
        self.down_left = [False] * (2 * n - 1)

        self.solv(0, board)
        return self.res
