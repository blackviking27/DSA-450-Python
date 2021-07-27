from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

# DFS functio to udpate the in-time and out-time of each node
# euler tour method
def dfs(node, parent, adj):
    global timer
    in_time[node] = timer
    timer += 1

    for v in adj[node]:
        if v != parent:
            dfs(v, node, adj)
    
    out_time[node] = timer
    timer += 1

# function to check wether a is subtree of b or not
def isSubTree(a, b):
    if in_time[b] > in_time[a] and out_time[b] < out_time[a]:
        return True
    else:
        return False

# Driver code
n = int(input())
# Creating the adjaceny matrix
adj = defaultdict(list)
for _ in range(n-1):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

timer = 1 # tells the time
in_time = [0]*(n + 1)
out_time = [0]*(n + 1)
dfs(1, 0, adj)

q = int(input())
for _ in range(q):
    d, x, y = list(map(int, input().split()))
    if d == 1:
        if isSubTree(y, x):
            print("YES")
        else:
            print("NO")
    else:
        if isSubTree(x, y):
            print("YES")
        else:
            print("NO")

