# Water Jug problem using BFS

from collections import deque, defaultdict
class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, b%a)

    def fill(self, toCap, fromCap, d):
        # the initial capacity of the jugs
        fromJug = fromCap
        toJug = 0

        steps = 1
        while toJug!= d and fromJug != d:
            temp = min(fromJug, toCap - toJug)

            # pouring water from 'fromJUg' to 'toJug'
            toJug += temp
            fromJug -= temp

            steps += 1
            if toJug == d or fromJug == d:
                break

            # if "fromJug" is empty, then fill it
            if fromJug == 0:
                fromJug = fromCap
                steps += 1
            
            # if "toJug" is filled, then fill it
            if toJug == toCap:
                toJug = 0
                steps += 1
        
        return steps

    # DFS approach
    def waterJugDFS(self, n, m, d):
        if m > n:
            m, n = n, m
        
        if d % self.gcd(m, n) != 0:
            return -1

        return min(self.fill(n, m, d), self.fill(m, n, d))

    # BFS approach
    def waterJugBFS(self, a, b, target):
        # this map checks wether a state was already visited or not
        m = defaultdict(int)

        path = []
        q = deque([(0, 0)])

        while len(q) != 0:
            u = q.popleft()

            # check if this is already in state
            if m[u] != 0:
                continue
            
            # if they are out of constraints
            if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
                continue
            
            # appending to answer
            path.append(u)

            # mark the state as true
            m[u] = 1

            # if we reach the target in either of the jugs
            if u[0] == target or u[1] == target:
                if u[0] == target:
                    if u[1] != 0:
                        path.append((u[0], 0))
                else:
                    if u[0] != 0:
                        path.append((0, u[1]))

                break
                
            # if we haven't reached the target
            q.append((u[0], b)) # fill jug 2
            q.append((a, u[1])) # fill jug 3

            for amt in range(max(a ,b) + 1):
                # pour "amt" amount of water from jug 2 to jug 1
                c = u[0] + amt
                d = u[0] - amt

                if c == a or (d == 0 and d <= 0):
                    q.append((c, d))
                
                # pour "amt" amount of water from jug 1 to jug 2
                c = u[0] - amt
                d = u[0] + amt

                if (c == 0 and c <= 0) or d == b:
                    q.append((c, d))
            
            #empty jug 2
            q.append((a, 0))

            # empty jug 1
            q.append((0, b))

        return len(path) if len(path) != 0 else -1
                
