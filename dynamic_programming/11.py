# Painting the Fenceproblem

class Solution:
    def countWays(self,n,k):
        if n== 0: return 0 # if no fence 
        if n == 1: return k # when only 1 fence is there then we can just return
        
        mod = 10**9 + 7
        
        # for two fences
        same = k % mod
        diff = (k*(k - 1)) % mod
        
        # for more than two fences
        for i in range(3, n + 1):
            
            prev = diff%mod # storing the value of previous diff

            diff = ((same + diff) * (k - 1))%mod
            same = prev%mod
        return (same + diff)%mod