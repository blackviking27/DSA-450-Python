# The Knight’s tour problem

class Solution:

    def solve(self, i, j, pos, board):
        # we are able to fill all the position
        if pos == self.n ** 2:
            return True

        # moving in the 8 directions
        for dx, dy in self.dir:

            x = i + dx  # new x position
            y = j + dy  # new y position

            # if x,y lie inside the board and that position is empty
            if x >= 0 and x < self.n and y >= 0 and y < self.n and board[x][y] == -1:

                board[x][y] = pos

                # if we are able to find a solution
                if self.solve(x, y, pos + 1, board):
                    return True

                # if we are not able to find a solution then we check for another position
                board[x][y] = -1

        # if not position give a  valid answer, then return false
        return False

    def knightTour(self, n):
        self.n = n

        # creating the board
        board = [[-1 for _ in range(n)] for _ in range(n)]

        # first position is zero
        board[0][0] = 0

        # possible 8 directions
        self.dir = [[-1, -2], [1, -2], [-2, -1], [-2, 1],
                    [-1, 2], [1, 2], [2, -1], [2, 1]]

        # now calling the function to solve
        self.solve(0, 0, 1, board)

        # printing the board
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()


s = Solution()
s.knightTour(8)
