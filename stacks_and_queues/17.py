# Length of the Longest Valid Substring

class Solution:
    def findMaxLen(self, string):
        stack = [-1]
        res = 0

        for i in range(len(string)):
            # for opening bracket
            if string[i] == '(':
                stack.append(i)
            # for closing bracket
            else:
                if len(stack) != 0:
                    stack.pop()
                
                if len(stack) != 0:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        
        return res
                    
