

from collections import defaultdict

def arrWithSumZero(arr, n):
    s = 0

    start = 0 # stores the firsy index of lengest sub array with sum 0
    end = 0 # stores the last index of lengest sub array with sum 0

    max_len = 0
    m = defaultdict(int)
    for i in range(n):
        s += arr[i]
        if s == 0:
            max_len = i + 1
            start = 0
            end = i
        elif m[s] == 0:
            m[s] = i 
        else:
            if max_len < i - m[s]:
                max_len = i - m[s]
                start = m[s] + 1
                end = i
    if max_len == 0:
        return False, 0, 0
    else:
        return True, start, end


def maxAreaRectWithSumZero(mat, row, col):
    top = bottom = left = right = 0
    max_area = float('-inf')
    for i in range(row):
        temp = [0]*col
        for j in range(i, row):
            for k in range(col):
                temp[k] += mat[j][k] if mat[k][j] else -1
            found, topRow, endRow = arrWithSumZero(temp, row)
            area = (j - 1 + 1) * (endRow - topRow + 1)
            if found and max_area < area:
                top = topRow
                bottom = endRow
                left = i
                right = j
                max_area = area
    print("(Top, bottom) : {}, {}".format(top, bottom))
    print("(left, right) : {}, {}".format(left, right))
    print("Max area {}".format(max_area))

# Driver code

row = 4
col = 4
mat = [[0, 0, 1, 1],
        [0, 1, 1, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 1]]

maxAreaRectWithSumZero(mat, row , col)
