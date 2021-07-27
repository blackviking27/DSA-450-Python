# Number of Triangles in a Directed and Undirected Graph

def countTriagles(graph, isDirected):
    n = len(graph)
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k and graph[i][j] and graph[j][k] and graph[k][i]:
                    count += 1
    
    if isDirected:
        return count // 3
    else:
        return count // 6

# driver code

graph = [[0, 1, 1, 0],
         [1, 0, 1, 1],
         [1, 1, 0, 1],
         [0, 1, 1, 0]]

digraph = [[0, 0, 1, 0],
           [1, 0, 0, 1],
           [0, 1, 0, 0],
           [0, 0, 1, 0]]

print(f"Number of triangles in undirected graph {countTriagles(graph, False)}")
print(f"Number of triangles in directed graph {countTriagles(digraph, True)}")