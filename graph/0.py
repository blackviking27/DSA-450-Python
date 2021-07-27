from collections import defaultdict

def adjacent_list(v, e):
    graph = [[] for i in range(v + 1)] # creating the vertices

    for _ in range(e):
        x, y = [int(x) for x in input("x, y: ").split()]
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, v + 1):
        print(f"{i} -->", *graph[i])

def adjacent_matrix(v, e):
    graph = [[0 for _ in range(v + 1)] for _ in range(v + 1)]

    for i in range(e):
        x, y = [int(x) for x in input("x, y: ").split()]
        graph[x][y] = 1
        graph[y][x] = 1
    
    for i in range(1, v + 1):
        print(f"{i} ==>", *graph[i])

v,e = [int(x) for x in input("Enter the vertices, edge: ").split()]

# using the adjacent list
adjacent_list(v, e)

# using the adjacent matrix
adjacent_matrix(v, e)