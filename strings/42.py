# Recursively print all sentences that can be formed from list of word lists

def print_recur(arr, m, n, output):
    
    # inserting the current word of row into the output
    output[m] = arr[m][n]
    
    # if we have reached the last row
    if m == row - 1:
        for i in range(column):
            print(output[i], end=" ")
        print()
        return
    
    # moving throught he next row
    for i in range(column):
        if arr[m + 1][i] != "":
            print_recur(arr, m + 1, i, output) 

def print_all(arr):
    
    output = [""] * row # stores one word from each row
    # considering every word of first array in 'arr' as the first word of sentence
    for i in range(column):
        if arr[0][i] != "":
            print_recur(arr, 0, i, output)

arr = [ ["you", "we",""],
        ["have", "are",""],
        ["sleep", "eat", "drink"]]

row = len(arr)
column = len(arr[0])
print_all(arr)