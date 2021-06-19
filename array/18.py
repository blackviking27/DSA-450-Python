# Common elements 
# Given three arrays sorted in increasing order. 
# Find the elements that are common in all three arrays.

class Solution:

    # used for mapping the elements
    def mapping(self, arr, m):
        for i in range(len(arr)):
            if arr[i] not in m:
                m[arr[i]] = 1
            else:
                m[arr[i]] += 1
        return m
    
    # Using a map
    # Time -> O(n1+n2+n3) Space -> O(n1 + n2 + n3)
    def commonElements1(self, a, b, c, n1, n2, n3):
        m1, m2, m3 = {}, {}, {} # map used to keep count of characters
        # mapping the elements in a,b and c respectively
        
        m1 = self.mapping(a, m1)
        m2 = self.mapping(b, m2)
        m3 = self.mapping(c, m3)
        
        res = []
        for i in range(n1):
            if a[i] in m1 and a[i] in m2 and a[i] in m3:
                res.append(a[i])
                m1.pop(a[i]) # removing the element from the amp
        
        return res
