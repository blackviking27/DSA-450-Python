# Next Smaller Element

def nextSmallerElement(arr, n):
    # stores the smallest element from the right
    stack = []

    res = [-1]*n
    for i in range(n - 1, -1, -1):
        # removing the element from the stack which are greater than the current element
        while stack and arr[i] < stack[-1]:
            stack.pop()

        # now updating the answer
        if len(stack) != 0:
            res[i] = stack[-1]

        # appending the current element to the stack
        stack.append(arr[i])

    return res


# driver code
# arr = [11, 13, 21, 3]
# arr = [13, 7, 6, 12]
arr = [4, 8, 5, 2, 25]
n = len(arr)
res = nextSmallerElement(arr, n)
for i in range(n):
    print(f"{arr[i]} --> {res[i]}")
