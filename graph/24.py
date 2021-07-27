# Snakes and Ladders

from collections import deque
class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        def label_to_position(label):
            #function is used to convert the labal to position on the board 
            # ex: label 2 would on position (n - 1, 1) on board
            # returns the quotient and remainder for label - 1 and n
            r, c = divmod(label - 1, n)
            if r % 2 == 0:
                return n - 1 -r, c
            else:
                return n - 1- r, n - 1 - c
        
        # stores the label that we have visited so far
        visited = set()
        
        q = deque([[1, 0]])
        
        while q:
            label, steps = q.popleft()
            r, c = label_to_position(label)
            
            if board[r][c] != -1:
                label = board[r][c]
            
            if label == n**2:
                return steps
            
            for i in range(1, 7):
                new_label = label + i
                if new_label <= n**2 and new_label not in visited:
                    visited.add(new_label)
                    q.append([new_label, steps + 1])
        return -1


