# Isomorphic Strings 

from collections import defaultdict

class Solution:
    def areIsomorphic(self, s1, s2):
        n = len(s1)
        m = len(s2)
        
        # if length is unequal
        if n != m: return 0

        m1 = defaultdict(str) # maps character of str1 to str2
        m2 = defaultdict(str) # maps character of str2 to str1
        
        for i in range(n):
            if m1[s1[i]] == "" and m2[s2[i]] == "":
                m1[s1[i]] = s2[i]       
                m2[s2[i]] = s1[i]
            elif m1[s1[i]] != s2[i]: return 0
        return 1

