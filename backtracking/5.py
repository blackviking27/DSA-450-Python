# M-Coloring Problem

def graphColoring(graph, V, m):
    # array to store color of each node
    color = [0] * V
    if solve(0, V, m, graph, color):
        return True
    return False


def solve(node, V, m, graph, color):
    # base case
    # we have traversed all the nodes and are able to assign colors
    if node == V:
        return True

    # trying to assign colors in range 1 to m
    for c in range(1, m + 1):
        # checks if we cab place color 'c' at the current node
        if isValid(node, c, V, graph, color):
            color[node] = c
            # if  we find a valid color for all other nodes then return true
            if solve(node + 1, V, m, graph, color):
                return True

            # we are not able associate colors to the node
            # thus we try other color
            color[node] = 0
    # if we are not able to assign color at all
    return False


def isValid(node, c, V, graph, color):
    for i in range(V):
        if graph[node][i] == 1 and color[i] == c:
            return False

    return False
