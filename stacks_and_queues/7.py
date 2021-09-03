# Special Stack 

def push(arr, ele):
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    arr.pop()

# function should return 1/0 or True/False
def isFull(n, arr):
    return len(arr) == n

# function should return 1/0 or True/False
def isEmpty(arr):
    return len(arr) == 0

# function should return minimum element from the stack
def getMin(n, arr):
    min_ele = float('inf')
    for el in arr:
        if el < min_ele:
            min_ele = el
    return min_ele