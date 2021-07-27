# Minimum Step by Knight

from collections import deque

class Solution:
    def minStepByKnight(self, KnightPos, TargetPos, n):
        x1, y1 = KnightPos
        x2, y2 = TargetPos

        if x1 == x2 and y1 == y2: # already at the target position
            return 0
        
        positions = deque([[x1-1, x2-1]]) # storing the positoin of the knight
        arr = [[0 for _ in range(n)] for _ in range(n)]

        directions = [[-1,-2], [1,-2],[-1, 2],[1,2], [-2,-1],[-2,1],[2,-1],[2,1]]

        while len(positions) != 0:
            temp = positions.popleft()
            i, j = temp
            for pos in directions:
                x = i + pos[0]
                y = j + pos[1]
                if x >= 0 and x < n and y >= 0 and y < n and arr[x][y] == 0:
                    arr[x][y] = arr[i][j] + 1
                    positions.append([x, y])
        return arr[x2-1][y2-1]