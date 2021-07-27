# Alien Dictionary

from collections import defaultdict
class Solution:
    def dfs(self, node):
        self.visited[node] = True

        for i in self.graph[node]:
            if not self.visited[i]:
                self.dfs(i)
        
        self.stack.append(node)

    def findOrder(self,dict, n, k):
        # creating a graph
        self.graph = defaultdict(list)

        for i in range(n - 1):
            w1 = dict[i]
            w2 = dict[i + 1]

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    self.graph[ord(w1[j]) - ord('a')].append(ord(w2[j]) - ord('a'))
                    break
        
        # topological sort
        self.visited = [False]*(k + 1)
        self.stack = []

        for i in range(k):
            if not self.visited[i]:
                self.dfs(i)
        
        return self.stack[::-1]

dictionary = ['baa' ,'abcd' ,'abca' ,'cab' ,'cada']
s = Solution()
print(s.findOrder(dictionary, 5, 4))