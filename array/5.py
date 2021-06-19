# Union of two arrays

class Solution:
    def union(self, a, n, b, m):
        # a -> arr, b -> arr
        # n -> a.len, m -> b.len
        occur = {}
        count = 0

        for i in range(n):
            if a[i] not in occur:
                occur[a[i]] = 1
                count += 1
                
        for i in range(m):
            if b[i] not in occur:
                occur[b[i]] = 1
                count += 1
        return count