# M-ColouringProblem

# function determines if the color of node is same as it's adjacent node or not
def isSafe(node, c, graph, V, color):
    for i in range(V):
        if graph[node][i] == 1 and color[i] == c:
            return False
    return True

# this function fills the color of the nodes and checks if it is valid or not
def colorGraph(node, V, graph, m, color):
    if node == V:
        return True
    
    # assinging color to node
    for c in range(1, m + 1):
        if isSafe(node, c, graph, V, color):
            color[node] = c

            if colorGraph(node + 1, V, graph, m, color):
                return True
            
            color[node] = 0 # backtracking from the current node

def graphColoring(graph, k, V):
    # tells the color of the node
    color = [0]*V

    if colorGraph(0, V, graph, k, color) == None:
        return False
    return True