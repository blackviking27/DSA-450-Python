# Journey to the Moon

# for one of the test cases
import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict
def dfs(node, visited, g):
    visited[node] = True
    global count
    count += 1
    for v in g[node]:
        if not visited[v]:
            dfs(v, visited, g)

count = 0
def journeyToMoon(n, astronaut):
    visited = [False]*n
    solution = [] # stores the number of astronaut in the same country
    g = defaultdict(list)

    for i in astronaut:
        g[i[0]].append(i[1])
        g[i[1]].append(i[0])
    
    for i in range(n):
        if not visited[i]:
            global count
            count = 0
            dfs(i, visited, g)
            solution.append(count)

    val = (n*(n-1)) // 2
    for i in solution:
        val -= (i*(i-1)) // 2
    return val

    
