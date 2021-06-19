# Min Number of Flips

class Solution:
    def minFlips(self, s):
        c1 = 0
        c2 = 0

        # for first case when even pos has 0 and odd pos has 1
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == '1':
                c1 += 1
            elif i % 2 != 0 and s[i] == '0':
                c1 += 1
        
        # for second case when even pos has 1 and odd pos has 0
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == '0':
                c2 += 1
            elif i % 2 != 0 and s[i] == '1':
                c2 += 1
        return min(c1, c2)