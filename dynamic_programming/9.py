# Gold Mine Problem 

class Solution:
    def maxSolution(self, n, m, arr):
        for col in range(m-2, -1, -1):
            for row in range(n):
                # taking the element on the right
                right =  arr[row][col + 1] # the next element
                
                # taking the diagonally up element on right
                if row == 0:
                    right_up = 0
                else:
                    right_up = arr[row - 1][col + 1] # taking diagonally up element
                
                # taking the diagonally down element on right
                if row == n-1:
                    right_down = 0
                else:
                    right_down = arr[row + 1][col + 1]
                
                arr[row][col] += max(right_up, right, right_down)
        
        max_gold = -1
        # max gold would be stored in the first column of any row
        for i in range(n):
            max_gold = max(max_gold, arr[i][0])
        
        return max_gold


