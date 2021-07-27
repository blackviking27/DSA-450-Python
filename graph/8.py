# Clone Graph

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors if neighbors is not None else []

from collections import deque
class Solution:
    def cloneGraphBFS(self, node):
        if node is None:
            return None

        q = deque([node])

        # mapping is used to map the old node to the new node
        # mapping[node] gives the new node which has the same value as node.val
        mapping = {node: Node(node.val, [])}

        while q:
            n = q.popleft()
            for i in n.neighbors:
                if i not in mapping:
                    mapping[i] = Node(i.val, [])
                    q.append(i)
                mapping[n].neighbors.append(mapping[i])
        return mapping[node]

    def cloneGraphDFS(self, node):
        if node is None:
            return None

        mapping = {}
        def dfs(node):
            if node in mapping:
                return mapping[node]
            
            mapping[node] = Node(node.val)
            for i in node.neighbors:
                mapping[node].neighbors.append(dfs(i))
            
            return mapping[node]
        
        return  dfs(node)