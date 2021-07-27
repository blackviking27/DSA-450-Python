# Maximum path sum in matrix 

class Solution:
    # this has the same approach as the gold mine problem but in this start from 
    # n-1 row and move along the column and take max of down, down left and down right value
    def maxPath(self, n, arr):
        for row in range(n-2, -1, -1):
            for col in range(n):
                down = arr[row+1][col] # taking the element just below the current element

                if col == 0:
                    down_left = 0
                else:
                    down_left = arr[row+1][col-1]
                
                if col == n-1:
                    down_right = 0
                else:
                    down_right = arr[row+1][col+1]
                
                arr[row][col] += max(down, down_left, down_right)
        
        max_sum = float('-inf')

        for i in range(n):
            max_sum = max(max_sum, arr[0][i])