# Factorials of large numbers 

class Solution:

    def multiply(self, x, res, res_size):
        carry = 0
        i = 0
        while i < res_size:
            prod = res[i] * x + carry
            res[i] = prod % 10
            carry = prod // 10
            i += 1
        
        # adding the carry to the list
        while carry:
            res[res_size] = carry % 10
            carry = carry // 10
            res_size += 1

        return res_size
        

    def factorial(self, n):
        res = [None]*(3000) # creating an array to store the answer
        res_size = 1

        x = 2
        while x <= n:
            res_size = self.multiply(x, res, res_size)
            x += 1
        ans = []
        for i in range(res_size - 1, - 1, -1):
            ans.append(res[i])
        return ans
