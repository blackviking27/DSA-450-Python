# 	Sum of minimum and maximum elements of all subarrays of size “k”.

from collections import deque


def SumOfKsubArray(arr, n, k):
    # greating 2 doubly ended queue
    s = deque()  # stores the element which are minimum for the window
    g = deque()  # stores the element which are maximum for the window

    # for first window
    for i in range(k):
        # removing the useless elements from both deques
        while len(s) > 0 and arr[i] <= arr[s[-1]]:
            s.pop()

        while len(g) > 0 and arr[i] >= arr[g[-1]]:
            g.pop()

        # appending the current element
        s.append(i)
        g.append(i)

    max_sum = 0  # stores the sum of min and max of a window

    # for the remaining windows
    for i in range(k, n):
        # calculating sum
        max_sum += arr[g[0]] + arr[s[0]]

        # removing elements which are not in the current window
        while len(s) > 0 and s[0] <= i - k:
            s.popleft()

        while len(g) > 0 and g[0] <= i - k:
            g.popleft()

        # removing the useless elements from the deques
        while len(s) > 0 and arr[i] <= arr[s[-1]]:
            s.pop()

        while len(g) > 0 and arr[i] >= arr[g[-1]]:
            g.pop()

        # appending the current element
        s.append(i)
        g.append(i)

    # for the last window
    max_sum += arr[s[0]] + arr[g[0]]
    return max_sum


# driver code
arr = [2, 5, -1, 7, -3, -1, -2]
n = len(arr)
k = 3
print(SumOfKsubArray(arr, n, k))
