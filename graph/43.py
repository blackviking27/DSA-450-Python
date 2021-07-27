# Two Clique Problem

def colorGraph(graph, color, src, c):
    if color[src] != -1 and color[src] != c:
        return False
    
    color[src] = c
    ans = True
    for i in range(len(graph)):
        if graph[src][i]:
            if color[i] == -1:
                ans &= colorGraph(graph, color, i, 1 - c)
            if color[i] != - 1 and color[i] != 1 -c:
                return False
        # at some point if was not possible to color the node
        if not ans:
            return False
    return True

def isBipartite(graph):
    color = [-1]*len(graph)
    return colorGraph(graph, color, 0, 1)

def canBeDividedInTwoCliques(graph, v):
    reverse_graph = [[None]*v for _ in range(v)]
    
    # reversing the original graph
    for i in range(v):
        for j in range(v):
            if i != j:
                reverse_graph[i][j] = 0 if graph[i][j] else 1
    
    return isBipartite(reverse_graph)

G = [[0, 1, 1, 1, 0], 
     [1, 0, 1, 0, 0], 
     [1, 1, 0, 0, 0], 
     [0, 1, 0, 0, 1],
     [0, 0, 0, 1, 0]]
v = 5
if canBeDividedInTwoCliques(G, v):
    print("YES")
else:
    print("NO")