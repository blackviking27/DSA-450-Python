# Count of number of given string in 2D character array

def solve(row, column, string, ch, idx):
    found = 0 # count the number of times we found the string
    if row >= 0 and column >= 0 and row < len(ch) and column < len(ch[0]) and string[idx] == ch[row][column]:
        temp = string[idx]
        ch[row][column] = 0
        idx += 1
        # if all the characters are found
        if idx == len(string):
            found = 1
        else:
            found += solve(row + 1, column, string, ch, idx)
            found += solve(row - 1, column, string, ch, idx)
            found += solve(row, column + 1, string, ch, idx)
            found += solve(row, column - 1, string, ch, idx)
        ch[row][column] = temp # putting the value back to original

    return found

# Driver code
ch = [['D','D','D','G','D','D'],
     ['B','B','D','E','B','S'],
     ['B','S','K','E','B','K'],
     ['D','D','D','D','D','E'],
     ['D','D','D','D','D','E'],
     ['D','D','D','D','D','G']]

string = 'GEEKS'
size = len(string)
matrix_size = len(ch)
ans = 0
for i in range(6):
    for j in range(6):
        # i, j => position of character in 2d array
        # the last parameter in the funtion is index of character in string
        ans += solve(i, j, string ,ch, 0)
print(ans)