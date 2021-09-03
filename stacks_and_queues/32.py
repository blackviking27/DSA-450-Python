# First negative integer in every window of size “k”

from collections import deque


def printFirstNegativeInteger(arr, n, k):
    ans = []
    q = deque()  # stores the index of the negative nnumbers

    # inserting the negative numbers from the first window of size k
    for i in range(k):
        if arr[i] < 0:
            q.append(i)

    # now moving for next windows
    for i in range(k, n):
        # getting the answer for previous  window

        # if Queue if empty then no negative exists in the previous window
        if not q:
            ans.append(0)
        else:
            ans.append(arr[q[0]])

        # removing the elements from the previous windows
        while q and q[0] <= i - k:
            q.popleft()

        # appednding the current element if it is negative
        if arr[i] < 0:
            q.append(i)
    if q:
        ans.append(arr[q[0]])
    else:
        ans.append(0)
    return ans
