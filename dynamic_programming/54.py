# Largest rectangular sub-matrix whose sum is 0

from collections import defaultdict 
def sumZero(arr, n):
    s = 0 # sum of the array
    ma = 1 # stores the max length
    mapping = defaultdict(int)

    for i in range(n):
        s += arr[i]
        if s == 0:
            ma = max(ma, i + 1)
        elif mapping[s]:
            ma = max(ma, i - mapping[s] + 1)
        else:
            mapping[s] = i
    
    return ma

def sumZeroMatrix(arr, row, col):
    max_rect = float('-inf') # stores the area of the triangle
    top = left = bottom = right = 0

    for i in range(row):
        ans = [0]*col
        for j in range(i, row):
            for c in range(col):
                ans[c] += arr[j][c]
            max_rect = max(max_rect, sumZero(ans, col) * (j - i + 1))
    return max_rect
            
# Driver code
arr = [[9, 7, 16, 5 ], [ 1, -6, -7, 3 ],
        [ 1, 8, 7, 9 ], [ 7, -2, 0, 10 ]]
row = 4
col = 4
print(sumZeroMatrix(arr, row, col))